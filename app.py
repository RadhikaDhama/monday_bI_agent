from monday_api import get_board_items
from analysis import (
    convert_to_dataframe,
    clean_data,
    pipeline_by_sector,
    top_deals
)
from agent import interpret_query, generate_insight
import pandas as pd
import streamlit as st 


DEALS_BOARD_ID = 5026983908
WORK_ORDERS_BOARD_ID = 5026983934

query = st.chat_input("Ask a business question")


print("\n[Agent Action] Understanding the user query...")
action = interpret_query(query)

print("Detected action:", action)


print("\n[Agent Action] Fetching monday boards...")

deals_data = get_board_items(DEALS_BOARD_ID)
work_orders_data = get_board_items(WORK_ORDERS_BOARD_ID)


print("\n[Agent Action] Converting to dataframes...")

deals_df = convert_to_dataframe(deals_data)
work_orders_df = convert_to_dataframe(work_orders_data)


print("\n[Agent Action] Cleaning data...")

deals_df = clean_data(deals_df)
work_orders_df = clean_data(work_orders_df)


combined_df = pd.concat([deals_df, work_orders_df], ignore_index=True)

print("Combined dataframe shape:", combined_df.shape)


print("\n[Agent Action] Running analysis...\n")


if "sector_pipeline" in action:

    result = pipeline_by_sector(combined_df)

    print(result)

    summary = result.to_string()

    insight = generate_insight(query, summary)

    print("\nAI Insight:\n")
    print(insight)


elif "top_deals" in action:

    result = top_deals(combined_df)

    print(result)

    summary = result.to_string()

    insight = generate_insight(query, summary)

    print("\nAI Insight:\n")
    print(insight)


else:

    print("Agent could not understand the query.")