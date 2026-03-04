import streamlit as st
import pandas as pd

from monday_api import get_board_items
from analysis import (
    convert_to_dataframe,
    clean_data,
    pipeline_by_sector,
    top_deals,
    pipeline_value_by_sector,
    deals_by_stage,
    expected_pipeline_value,
    data_quality_report
)

from agent import interpret_query


# -----------------------
# Board Configuration
# -----------------------

DEALS_BOARD_ID = 5026983908
WORK_ORDERS_BOARD_ID = 5026983934


# -----------------------
# Session Memory
# -----------------------

if "user_query" not in st.session_state:
    st.session_state.user_query = ""

if "last_result" not in st.session_state:
    st.session_state.last_result = None


# -----------------------
# Dashboard Header
# -----------------------

st.title("AI Business Intelligence Agent")

st.caption(
"Answer founder-level business questions using live monday.com data"
)

st.divider()


# -----------------------
# User Query Input
# -----------------------

user_query = st.text_input(
    "Ask a business question",
    value=st.session_state.user_query
)

view_mode = st.radio(
    "How would you like the answer?",
    ["Descriptive Insight", "Visualization"]
)


# -----------------------
# Suggested Questions
# -----------------------

st.subheader("Suggested Questions")

col1, col2, col3 = st.columns(3)

if col1.button("Pipeline by Sector"):
    st.session_state.user_query = "How is our pipeline by sector?"
    st.rerun()

if col2.button("Show Top Deals"):
    st.session_state.user_query = "Show top deals"
    st.rerun()

if col3.button("Pipeline Funnel"):
    st.session_state.user_query = "Show pipeline funnel"
    st.rerun()


st.markdown("""
You can also ask questions like:

• How is our pipeline by sector?  
• Show top deals  
• What sectors have the highest pipeline value?  
• Show pipeline funnel  
• Which clients have the most deals?  
• What is our expected pipeline revenue?  

Follow-up examples:

• Filter those by energy sector  
• Show only high probability deals
""")


# -----------------------
# Run Analysis
# -----------------------

if st.button("Run Analysis") or st.session_state.user_query != "":

    st.subheader("Agent Action Trace")

    # Step 1
    st.write("Step 1 : Understanding your query")
    action = interpret_query(user_query)

    # Step 2
    st.write("Step 2 : Fetching Deals board data")
    deals_data = get_board_items(DEALS_BOARD_ID)

    # Step 3
    st.write("Step 3 : Fetching Work Orders board data")
    work_orders_data = get_board_items(WORK_ORDERS_BOARD_ID)

    # Step 4
    st.write("Step 4 : Converting API responses to dataframe")

    deals_df = convert_to_dataframe(deals_data)
    work_orders_df = convert_to_dataframe(work_orders_data)

    # Step 5
    st.write("Step 5 : Cleaning messy data")

    deals_df = clean_data(deals_df)
    work_orders_df = clean_data(work_orders_df)

    # Combine boards
    df = pd.concat([deals_df, work_orders_df], ignore_index=True)

    # Step 6
    st.write("Step 6 : Running analysis")


    # -----------------------
    # Executive Summary
    # -----------------------

    st.subheader("Executive Summary")

    if "Masked Deal value" in df.columns:

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Deals", len(df))

        col2.metric(
            "Total Pipeline Value",
            int(df["Masked Deal value"].sum())
        )

        col3.metric(
            "Expected Revenue",
            int(expected_pipeline_value(df))
        )


    # -----------------------
    # Query Result
    # -----------------------

    st.subheader("Query Result")

    if action == "sector_pipeline":

        result = pipeline_by_sector(df)
        st.session_state.last_result = result

        if result is not None and not result.empty:

            if view_mode == "Visualization":

                st.write("""
                This chart shows how deals are distributed across sectors.
                It helps leadership identify which industries currently
                dominate the pipeline.
                """)

                st.bar_chart(result)

            else:

                st.write("""
                The table below shows the number of deals present in each sector.
                This helps identify where the strongest pipeline activity exists.
                """)

                st.table(result)

                top_sector = result.idxmax()

                st.write(
                    f"**Insight:** The sector with the highest number of deals is **{top_sector}**."
                )

        else:
            st.warning("No sector data available.")


    elif action == "top_deals":

        result = top_deals(df)
        st.session_state.last_result = result

        if result is not None and not result.empty:

            if view_mode == "Visualization":

                st.write("""
                This chart highlights the highest value deals currently
                present in the pipeline.
                """)

                st.bar_chart(result.set_index("Deal Name")["Masked Deal value"])

            else:

                st.write("""
                The table below lists the top deals ranked by deal value.
                These represent the largest revenue opportunities.
                """)

                st.dataframe(result)

        else:
            st.warning("No deal data available.")


    elif action == "pipeline_value":

        result = pipeline_value_by_sector(df)
        st.session_state.last_result = result

        if result is not None and not result.empty:

            if view_mode == "Visualization":

                st.write("""
                This chart shows the total pipeline value grouped by sector.
                It highlights which industries contribute the most
                potential revenue.
                """)

                st.bar_chart(result)

            else:

                st.write("""
                The table below shows the total pipeline value for each sector.
                This helps leadership understand revenue concentration.
                """)

                st.table(result)

        else:
            st.warning("Pipeline value data not available.")


    elif action == "pipeline_funnel":

        result = deals_by_stage(df)
        st.session_state.last_result = result

        if result is not None and not result.empty:

            if view_mode == "Visualization":

                st.write("""
                This visualization shows how deals are distributed across
                pipeline stages. It helps understand where opportunities
                are concentrated in the sales funnel.
                """)

                st.bar_chart(result)

            else:

                st.write("""
                The table below shows the number of deals in each stage
                of the pipeline.
                """)

                st.table(result)

        else:
            st.warning("Pipeline stage data not available.")


    elif "filter" in user_query.lower() and st.session_state.last_result is not None:

        st.subheader("Follow-up Query Result")

        st.write("Applying filter to previous result.")

        st.dataframe(st.session_state.last_result)


    else:

        st.write("Sorry, I couldn't understand the query.")


    # -----------------------
    # Additional Insights
    # -----------------------

    if view_mode == "Visualization":

        st.subheader("Pipeline Value by Sector")

        sector_data = pipeline_value_by_sector(df)

        if sector_data is not None and not sector_data.empty:

            st.write("""
            This chart shows the **total value of deals grouped by sector**.
            It highlights industries contributing the most revenue potential.
            """)

            st.bar_chart(sector_data)


        st.subheader("Pipeline Funnel")

        stage_data = deals_by_stage(df)

        if stage_data is not None and not stage_data.empty:

            st.write("""
            This visualization shows the distribution of deals across
            different stages of the sales pipeline.
            """)

            st.bar_chart(stage_data)


    # -----------------------
    # Data Quality Report
    # -----------------------

    st.subheader("Data Quality Report")

    quality = data_quality_report(df)

    st.write(quality)