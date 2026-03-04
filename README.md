# AI Business Intelligence Agent

An **AI-powered Business Intelligence assistant** that answers business questions using **Monday.com pipeline data**.
Users can ask questions in natural language, and the system automatically analyzes CRM data and generates insights.

---

##  Features

* Connects to the **Monday.com API** to fetch pipeline data
* Cleans and structures messy CRM data
* Performs **automated business intelligence analysis**
* Understands **natural language queries**
* Uses an **LLM to classify business questions**
* Generates **AI-powered insights**
* Displays results interactively with **Streamlit**

---

##  Supported Analytics

The agent currently supports the following analyses:

* **Pipeline by Sector**
  Number of deals grouped by sector.

* **Pipeline Value by Sector**
  Total deal value grouped by sector.

* **Top Deals**
  Largest deals currently present in the pipeline.

* **Expected Pipeline Value**
  Weighted pipeline value calculated using deal probabilities.

* **Deals by Stage**
  Pipeline funnel showing number of deals in each stage.

* **Top Clients**
  Clients with the highest number of deals.

---

##  Example Questions

You can ask questions like:

* Show the number of deals by sector
* What is the pipeline value by sector?
* Show the top deals in the pipeline
* What is the expected pipeline value?
* How many deals are in each stage?
* Which clients have the most deals?

---

##  Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Groq LLM (Llama 3.1)**
* **Monday.com API**

---

##  How It Works

1. The user asks a **business question** in the Streamlit interface.
2. An **LLM classifies the question** into a predefined BI action.
3. The system **fetches pipeline data** from Monday.com.
4. Data is **cleaned and structured using Pandas**.
5. The relevant **analysis function runs** on the dataset.
6. The LLM generates a **clear business insight** from the analysis results.

---

##  Project Structure

```
project/
│
├── app.py                # Streamlit application
├── agent.py              # LLM query interpretation + insight generation
├── analysis.py           # Business intelligence analysis functions
├── monday_api.py         # Monday.com API integration
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

##  Running the Project

1. Install dependencies

```
pip install -r requirements.txt
```

2. Add your **Groq API key** to Streamlit secrets.

3. Run the Streamlit app

```
streamlit run app.py
```

---

##  Deployment

This project can be easily deployed using **Streamlit Cloud**.

Steps:

1. Push the project to GitHub
2. Connect the repository to **Streamlit Cloud**
3. Add the **GROQ_API_KEY** in Streamlit secrets
4. Deploy the app

---

##  Future Improvements

* Add conversational memory for follow-up questions
* Support more BI queries and analytics
* Improve query classification accuracy
* Add visualizations for pipeline insights
* Build a dashboard for historical pipeline trends


## Live App
https://mondaybiagent-55uhppy5jirggqvtaynd2r.streamlit.app/

## Architecture

User Query → LLM Classifies Intent → Fetch monday.com Data → Clean Data → Run BI Analysis → Generate Insight → Display Results

<img width="1152" height="776" alt="image" src="https://github.com/user-attachments/assets/9559e974-b622-49d9-abe8-29dde98edfec" />
<img width="1197" height="760" alt="image" src="https://github.com/user-attachments/assets/b619697c-d3c1-4899-bca6-03563c4a0593" />
<img width="1236" height="646" alt="image" src="https://github.com/user-attachments/assets/62febd52-9751-4f65-9185-f9ce70e0bf0e" />
<img width="1181" height="791" alt="image" src="https://github.com/user-attachments/assets/902b7816-bdc6-4a5d-a270-d0d6e3c3e4e1" />
<img width="1236" height="638" alt="image" src="https://github.com/user-attachments/assets/2681bfea-1934-45ff-b5fc-dc1cbabb06b9" />
<img width="1190" height="632" alt="image" src="https://github.com/user-attachments/assets/9515e1df-27cf-4996-96a1-4fd87e226e79" />
<img width="1159" height="657" alt="image" src="https://github.com/user-attachments/assets/d0b4317a-d2e7-41b1-9f95-3756e386d261" />
<img width="1288" height="633" alt="image" src="https://github.com/user-attachments/assets/8beed9c5-3f28-431c-a37e-1f582746f68f" />








