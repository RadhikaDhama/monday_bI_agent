# AI Business Intelligence Agent for Monday.com

This project builds an AI-powered BI assistant that answers business questions using monday.com pipeline data.

## Features
- Connects to monday.com API
- Cleans messy CRM data
- Runs business intelligence analysis
- Understands natural language queries
- Generates AI insights using LLM

## Example Questions
- Show top deals
- What sectors have the most pipeline?
- How is the pipeline distributed?

## Tech Stack
- Python
- Streamlit
- Pandas
- Groq LLM
- Monday.com API

## Live App
https://mondaybiagent-55uhppy5jirggqvtaynd2r.streamlit.app/

## Architecture

User Query → LLM Classifies Intent → Fetch monday.com Data → Clean Data → Run BI Analysis → Generate Insight → Display Results
