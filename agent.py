from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def interpret_query(query):
    """
    Classify the user query into a BI action.
    """

    prompt = f"""
You are a business intelligence agent for analyzing sales pipeline data.

Classify the user question into EXACTLY one of the following actions:

pipeline_by_sector
pipeline_value_by_sector
top_deals
expected_pipeline_value
deals_by_stage
top_clients
unknown

Action definitions:

pipeline_by_sector → number of deals grouped by sector

pipeline_value_by_sector → total deal value grouped by sector

top_deals → largest deals in the pipeline

expected_pipeline_value → weighted pipeline value based on deal probability

deals_by_stage → number of deals in each deal stage (pipeline funnel)

top_clients → clients with the highest number of deals

unknown → if the question is unrelated to pipeline or deal analytics

Return ONLY the action name.

User Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    action = response.choices[0].message.content.strip().lower()

    return action


def generate_insight(question, data_summary):
    """
    Generate a business insight based on analysis results.
    """

    prompt = f"""
You are a business intelligence analyst.

A founder asked the following question:

{question}

Here is the analyzed data:

{data_summary}

Explain the insight clearly in simple business language.
Do not repeat the raw numbers unless necessary.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    insight = response.choices[0].message.content.strip()


    return insight

