import streamlit as st
import pandas as pd

from monday_api import get_board_items
from analysis import (
    convert_to_dataframe,
    clean_data,
    pipeline_by_sector,
    top_deals
)
from agent import interpret_query, generate_insight


DEALS_BOARD_ID = 5026983908
WORK_ORDERS_BOARD_ID = 5026983934


st.title("AI Business Intelligence Agent")

st.write("Ask questions about your Monday.com pipeline data.")


# Chat input
query = st.chat_input("Ask a business question")


# Only run when user sends a message
if query:

    # Show user message
    with st.chat_message("user"):
        st.write(query)

    with st.spinner("AI analyzing business data..."):

        # Step 1 — Understand query
        action = interpret_query(query)

        # Step 2 — Fetch monday data
        deals_data = get_board_items(DEALS_BOARD_ID)
        work_orders_data = get_board_items(WORK_ORDERS_BOARD_ID)

        # Step 3 — Convert to dataframe
        deals_df = convert_to_dataframe(deals_data)
        work_orders_df = convert_to_dataframe(work_orders_data)

        # Step 4 — Clean data
        deals_df = clean_data(deals_df)
        work_orders_df = clean_data(work_orders_df)

        # Step 5 — Combine datasets
        combined_df = pd.concat([deals_df, work_orders_df], ignore_index=True)


        # Step 6 — Run analysis
        if "sector_pipeline" in action:

            result = pipeline_by_sector(combined_df)
            summary = result.to_string()

        elif "top_deals" in action:

            result = top_deals(combined_df)
            summary = result.to_string()

        else:

            result = None
            summary = "Agent could not understand the query."


        # Step 7 — Generate AI insight
        if result is not None:
            insight = generate_insight(query, summary)
        else:
            insight = "I couldn't understand the question. Try asking about pipeline by sector or top deals."


    # Display assistant response
    with st.chat_message("assistant"):

        if isinstance(result, pd.DataFrame) or isinstance(result, pd.Series):
            st.write("### Data Result")
            st.dataframe(result)

        st.write("### AI Insight")

        st.write(insight)

