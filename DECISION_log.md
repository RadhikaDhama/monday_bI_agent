# Decision Log

**Project:** Monday.com Business Intelligence Agent
**Objective:** Build an AI-powered assistant that can answer business intelligence questions using live Monday.com pipeline data.

---

# 1. Problem Interpretation

The goal of this project was to build an AI assistant that can answer **founder-level business questions** using operational data stored in Monday.com boards.

The boards available for this project contain information about **Deals** and **Work Orders**, which together represent the company’s sales pipeline and operational activities.

In real-world scenarios, founders and business leaders often ask questions like:

* "Which sector has the strongest pipeline?"
* "Show the top deals right now."
* "How many deals are in each stage?"
* "What is the expected pipeline value?"

These questions are typically asked in **natural language**, not in technical terms.
Therefore, the system needed to be capable of both **understanding human questions** and **performing structured data analysis**.

To solve this, the system performs five key tasks:

1. Fetch live data from Monday.com boards
2. Clean and organize messy CRM-style data
3. Understand the user’s question using an LLM
4. Run the correct business analysis
5. Present the result in a simple and understandable way

---

# 2. Architecture Decision

The system was designed using a **hybrid approach**, combining:

* Large Language Models (LLMs)
* Deterministic Python analytics

This design separates **language understanding** from **numerical analysis**.

### System Flow

User Question
↓
LLM understands the intent
↓
Fetch Monday.com data
↓
Clean and structure the data
↓
Run the appropriate analysis
↓
Generate business insight using LLM
↓
Display results in Streamlit

### Why this approach was chosen

LLMs are very good at understanding **natural language**, but they are not reliable for **mathematical or numerical calculations**.

Therefore:

* The **LLM is used for understanding the question and generating insights**
* **Python and Pandas handle all data analysis**

This ensures that the results remain **accurate and deterministic**.

---

# 3. Monday.com Integration

The system connects to Monday.com using its **GraphQL API**.

Two boards are used:

* **Deals Board**
* **Work Orders Board**

Whenever a user asks a question, the system fetches **live data** from these boards.

Example workflow:

User Query
→ Fetch Deals Board
→ Fetch Work Orders Board
→ Convert data to DataFrames
→ Combine the datasets

This ensures that the insights are always based on the **latest available data**.

---

# 4. Data Cleaning Strategy

CRM data is rarely clean or perfectly structured.
To handle this, a **data cleaning pipeline** was implemented.

Some common issues addressed include:

* Missing values
* Inconsistent sector names
* Numeric values stored as text
* Probability fields stored as strings
* Structural differences between boards

### Cleaning steps performed

* Replace missing values with `"Unknown"`
* Convert deal values into numeric format
* Normalize sector names
* Convert probability values into numeric percentages
* Merge multiple datasets into one unified dataset

This step ensures the analysis remains **stable even when the source data is imperfect**.

---

# 5. Query Understanding

Users can ask questions in many different ways. Writing manual rules for every possible phrasing would be difficult.

Instead, the system uses an **LLM (Llama 3.1 via Groq)** to classify questions into predefined actions.

### Supported analytical actions

| Action                     | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `pipeline_by_sector`       | Number of deals grouped by sector                 |
| `pipeline_value_by_sector` | Total deal value grouped by sector                |
| `top_deals`                | Largest deals currently in the pipeline           |
| `expected_pipeline_value`  | Weighted pipeline value based on deal probability |
| `deals_by_stage`           | Distribution of deals across pipeline stages      |
| `top_clients`              | Clients with the highest number of deals          |
| `unknown`                  | Query unrelated to pipeline analytics             |

Example:

| User Question                           | Action                     |
| --------------------------------------- | -------------------------- |
| "Show deals by sector"                  | `pipeline_by_sector`       |
| "What is the pipeline value by sector?" | `pipeline_value_by_sector` |
| "Show the biggest deals"                | `top_deals`                |

The LLM converts the natural language question into one of these actions, which then triggers the appropriate Python analysis.

---

# 6. Business Intelligence Analysis

Once the intent is identified, the system runs the corresponding **analysis function** on the cleaned dataset.

### Implemented analyses

**Pipeline by Sector**
Counts the number of deals grouped by sector.

**Pipeline Value by Sector**
Calculates the total deal value for each sector.

**Top Deals**
Shows the largest deals currently in the pipeline.

**Expected Pipeline Value**
Calculates the weighted value of deals based on their probability of closing.

**Deals by Stage**
Shows the distribution of deals across pipeline stages.

**Top Clients**
Identifies clients with the highest number of deals.

These analyses represent the types of insights that **founders and leadership teams commonly need**.

---

# 7. Insight Generation

After the analysis is completed, the results are summarized and sent to the LLM.

The LLM then converts the raw data into **clear business insights**.

Example:

Input (analysis result):

Top Deals Table

Output:

> "The pipeline is currently driven by a few large deals, indicating strong potential revenue concentration."

This step makes the results easier for **non-technical stakeholders** to understand.

---

# 8. User Interface

The interface was built using **Streamlit**.

Streamlit was chosen because it allows rapid development of **interactive data applications using Python**.

Key interface features include:

* Chat-style question input
* Structured data tables
* AI-generated insight summaries
* Simple and intuitive layout

---

# 9. Deployment

The project was deployed using **Streamlit Community Cloud**.

Reasons for choosing this platform:

* Easy integration with GitHub
* Automatic updates when code is pushed
* Built-in secrets management
* No infrastructure setup required

Sensitive API keys are stored securely using:

```python
st.secrets["GROQ_API_KEY"]
st.secrets["MONDAY_API_KEY"]
```

This prevents credentials from being exposed in the repository.

---

# 10. Limitations

Due to time and scope constraints, some limitations remain.

### Limited question scope

The agent currently supports only a defined set of analytics queries.

### No conversational memory

Users cannot yet ask follow-up questions referencing previous results.

### Basic visualizations

The system focuses primarily on tabular outputs rather than complex dashboards.

---

# 11. Future Improvements

With further development, several enhancements could be added:

* Support for follow-up conversational queries
* Predictive pipeline forecasting
* More advanced data visualizations
* Automated executive reports
* Integration with additional data sources

---

# Conclusion

This project demonstrates how **AI agents can combine natural language understanding with real operational data to provide business intelligence insights**.

By combining:

* LLM-based query interpretation
* live Monday.com data integration
* structured Python analytics
* conversational outputs

the system provides a strong foundation for **AI-driven business decision support tools**.
