from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def interpret_query(query):
    """
    Classify the user query into a BI action.
    """

    prompt = f"""
You are a business intelligence agent.

Classify the user question into EXACTLY one of these actions:

sector_pipeline
top_deals
pipeline_value
pipeline_funnel

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