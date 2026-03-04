import requests
import os
import streamlit as st

API_KEY = st.secrets["MONDAY_API_KEY"]
print("Loaded Monday API Key:", API_KEY)

url = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}


def get_board_items(board_id):

    query = f"""
    {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(url, json={"query": query}, headers=headers)

    data = response.json()

    if "errors" in data:
        print("Monday API Error:", data["errors"])
        return {}

    return data