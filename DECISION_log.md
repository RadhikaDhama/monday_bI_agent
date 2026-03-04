# Decision Log

**Project:** Monday.com Business Intelligence Agent  
**Objective:** Build an AI-powered agent capable of answering founder-level business intelligence questions using live monday.com board data.

---

# 1. Problem Interpretation

The goal of the project was to build an AI agent capable of answering business questions using operational data stored in monday.com boards. The boards provided contained **Deals** and **Work Orders** data representing pipeline and project execution information.

Founders and executives typically ask **high-level natural language questions**, such as:

- "How is our pipeline looking for the energy sector?"
- "Show top deals."
- "Which sector has the strongest pipeline?"

To address this, the system needed to perform the following tasks:

1. Fetch **live data from monday.com boards**
2. Clean and normalize messy operational data
3. Interpret natural language queries
4. Run business intelligence analysis
5. Present insights in a clear and understandable format

---

# 2. Architecture Decision

A **hybrid architecture** was chosen combining:

- **Large Language Model reasoning**
- **Deterministic Python analytics**

This architecture separates **language understanding** from **numerical computation**.

### System Flow

User Question  
↓  
LLM Intent Classification  
↓  
Fetch monday.com Data via API  
↓  
Data Cleaning and Normalization  
↓  
Business Intelligence Analysis  
↓  
LLM Insight Generation  
↓  
Streamlit Interface Output

### Reasoning

The LLM is used only for:

- interpreting natural language queries
- generating business-friendly insights

All numerical analysis is performed using **Python and Pandas**, which ensures accuracy and avoids hallucinated results from the LLM.

---

# 3. Monday.com Integration

The system integrates with monday.com using the **GraphQL API**.

Two boards are queried:

- Deals Board
- Work Orders Board

Every user query triggers **live API calls**, ensuring that the agent always works with the most recent operational data.

Example workflow:

User Query → Fetch Deals Board → Fetch Work Orders Board → Combine datasets

This approach avoids stale data and ensures real-time analysis.

---

# 4. Data Resilience Strategy

Operational CRM-style data is often inconsistent. Therefore, a **data cleaning pipeline** was implemented.

### Data quality issues handled

- Missing values
- Inconsistent sector names
- Text-based numeric fields
- Probability fields stored as text
- Structural differences between boards

### Cleaning steps implemented

- Replace missing values with `"Unknown"`
- Convert deal values to numeric using `pandas.to_numeric`
- Normalize sector names
- Convert closure probability text values into numeric scores
- Merge data from multiple boards into a unified dataset

This ensures the system remains robust even when working with incomplete or inconsistent records.

---

# 5. Query Understanding Approach

Founder-level questions can be phrased in many ways, making rule-based parsing unreliable.

To address this, the system uses an **LLM (Llama 3 via Groq API)** to classify queries into predefined analytical actions.

Example mapping:

| User Question | Action |
|---------------|--------|
| "show top deals" | `top_deals` |
| "pipeline by sector" | `sector_pipeline` |
| "sector distribution of deals" | `sector_pipeline` |

The LLM converts natural language into structured commands that trigger specific Python analytics functions.

This allows flexible query phrasing without complex rule engineering.

---

# 6. Business Intelligence Layer

Once the intent is detected, Python functions perform structured analysis on the cleaned dataset.

Key analytics implemented include:

### Pipeline by Sector
Counts the number of deals grouped by industry sector.

### Top Deals
Identifies the highest-value deals currently in the pipeline.

### Pipeline Value by Sector
Calculates the total deal value aggregated by sector.

### Pipeline Funnel
Shows distribution of deals across pipeline stages.

These analytics represent the types of insights typically required by leadership teams.

---

# 7. Insight Generation

After analytics are computed, the results are summarized and passed to the LLM to generate **natural-language business insights**.

Example:

Input:  
Top deals table

LLM Output:  
"The pipeline is currently dominated by infrastructure and energy deals, indicating strong sectoral demand."

This step converts raw numerical analysis into **clear executive-level insights**.

---

# 8. User Interface Design

The interface was built using **Streamlit** due to its ability to quickly build interactive data applications.

Advantages of Streamlit:

- rapid development
- interactive UI components
- easy integration with Python data libraries
- straightforward deployment

Key interface features include:

- conversational query input
- structured data tables
- automatic visualizations
- AI-generated insight summaries

---

# 9. Deployment Strategy

The application was deployed using **Streamlit Community Cloud**.

Reasons for choosing Streamlit Cloud:

- simple deployment process
- GitHub integration
- automatic updates on code push
- secure secrets management

API credentials are stored using:
# Decision Log

**Project:** Monday.com Business Intelligence Agent  
**Objective:** Build an AI-powered agent capable of answering founder-level business intelligence questions using live monday.com board data.

---

# 1. Problem Interpretation

The goal of the project was to build an AI agent capable of answering business questions using operational data stored in monday.com boards. The boards provided contained **Deals** and **Work Orders** data representing pipeline and project execution information.

Founders and executives typically ask **high-level natural language questions**, such as:

- "How is our pipeline looking for the energy sector?"
- "Show top deals."
- "Which sector has the strongest pipeline?"

To address this, the system needed to perform the following tasks:

1. Fetch **live data from monday.com boards**
2. Clean and normalize messy operational data
3. Interpret natural language queries
4. Run business intelligence analysis
5. Present insights in a clear and understandable format

---

# 2. Architecture Decision

A **hybrid architecture** was chosen combining:

- **Large Language Model reasoning**
- **Deterministic Python analytics**

This architecture separates **language understanding** from **numerical computation**.

### System Flow

User Question  
↓  
LLM Intent Classification  
↓  
Fetch monday.com Data via API  
↓  
Data Cleaning and Normalization  
↓  
Business Intelligence Analysis  
↓  
LLM Insight Generation  
↓  
Streamlit Interface Output

### Reasoning

The LLM is used only for:

- interpreting natural language queries
- generating business-friendly insights

All numerical analysis is performed using **Python and Pandas**, which ensures accuracy and avoids hallucinated results from the LLM.

---

# 3. Monday.com Integration

The system integrates with monday.com using the **GraphQL API**.

Two boards are queried:

- Deals Board
- Work Orders Board

Every user query triggers **live API calls**, ensuring that the agent always works with the most recent operational data.

Example workflow:

User Query → Fetch Deals Board → Fetch Work Orders Board → Combine datasets

This approach avoids stale data and ensures real-time analysis.

---

# 4. Data Resilience Strategy

Operational CRM-style data is often inconsistent. Therefore, a **data cleaning pipeline** was implemented.

### Data quality issues handled

- Missing values
- Inconsistent sector names
- Text-based numeric fields
- Probability fields stored as text
- Structural differences between boards

### Cleaning steps implemented

- Replace missing values with `"Unknown"`
- Convert deal values to numeric using `pandas.to_numeric`
- Normalize sector names
- Convert closure probability text values into numeric scores
- Merge data from multiple boards into a unified dataset

This ensures the system remains robust even when working with incomplete or inconsistent records.

---

# 5. Query Understanding Approach

Founder-level questions can be phrased in many ways, making rule-based parsing unreliable.

To address this, the system uses an **LLM (Llama 3 via Groq API)** to classify queries into predefined analytical actions.

Example mapping:

| User Question | Action |
|---------------|--------|
| "show top deals" | `top_deals` |
| "pipeline by sector" | `sector_pipeline` |
| "sector distribution of deals" | `sector_pipeline` |

The LLM converts natural language into structured commands that trigger specific Python analytics functions.

This allows flexible query phrasing without complex rule engineering.

---

# 6. Business Intelligence Layer

Once the intent is detected, Python functions perform structured analysis on the cleaned dataset.

Key analytics implemented include:

### Pipeline by Sector
Counts the number of deals grouped by industry sector.

### Top Deals
Identifies the highest-value deals currently in the pipeline.

### Pipeline Value by Sector
Calculates the total deal value aggregated by sector.

### Pipeline Funnel
Shows distribution of deals across pipeline stages.

These analytics represent the types of insights typically required by leadership teams.

---

# 7. Insight Generation

After analytics are computed, the results are summarized and passed to the LLM to generate **natural-language business insights**.

Example:

Input:  
Top deals table

LLM Output:  
"The pipeline is currently dominated by infrastructure and energy deals, indicating strong sectoral demand."

This step converts raw numerical analysis into **clear executive-level insights**.

---

# 8. User Interface Design

The interface was built using **Streamlit** due to its ability to quickly build interactive data applications.

Advantages of Streamlit:

- rapid development
- interactive UI components
- easy integration with Python data libraries
- straightforward deployment

Key interface features include:

- conversational query input
- structured data tables
- automatic visualizations
- AI-generated insight summaries

---

# 9. Deployment Strategy

The application was deployed using **Streamlit Community Cloud**.

Reasons for choosing Streamlit Cloud:

- simple deployment process
- GitHub integration
- automatic updates on code push
- secure secrets management

API credentials are stored using:
# Decision Log

**Project:** Monday.com Business Intelligence Agent  
**Objective:** Build an AI-powered agent capable of answering founder-level business intelligence questions using live monday.com board data.

---

# 1. Problem Interpretation

The goal of the project was to build an AI agent capable of answering business questions using operational data stored in monday.com boards. The boards provided contained **Deals** and **Work Orders** data representing pipeline and project execution information.

Founders and executives typically ask **high-level natural language questions**, such as:

- "How is our pipeline looking for the energy sector?"
- "Show top deals."
- "Which sector has the strongest pipeline?"

To address this, the system needed to perform the following tasks:

1. Fetch **live data from monday.com boards**
2. Clean and normalize messy operational data
3. Interpret natural language queries
4. Run business intelligence analysis
5. Present insights in a clear and understandable format

---

# 2. Architecture Decision

A **hybrid architecture** was chosen combining:

- **Large Language Model reasoning**
- **Deterministic Python analytics**

This architecture separates **language understanding** from **numerical computation**.

### System Flow

User Question  
↓  
LLM Intent Classification  
↓  
Fetch monday.com Data via API  
↓  
Data Cleaning and Normalization  
↓  
Business Intelligence Analysis  
↓  
LLM Insight Generation  
↓  
Streamlit Interface Output

### Reasoning

The LLM is used only for:

- interpreting natural language queries
- generating business-friendly insights

All numerical analysis is performed using **Python and Pandas**, which ensures accuracy and avoids hallucinated results from the LLM.

---

# 3. Monday.com Integration

The system integrates with monday.com using the **GraphQL API**.

Two boards are queried:

- Deals Board
- Work Orders Board

Every user query triggers **live API calls**, ensuring that the agent always works with the most recent operational data.

Example workflow:

User Query → Fetch Deals Board → Fetch Work Orders Board → Combine datasets

This approach avoids stale data and ensures real-time analysis.

---

# 4. Data Resilience Strategy

Operational CRM-style data is often inconsistent. Therefore, a **data cleaning pipeline** was implemented.

### Data quality issues handled

- Missing values
- Inconsistent sector names
- Text-based numeric fields
- Probability fields stored as text
- Structural differences between boards

### Cleaning steps implemented

- Replace missing values with `"Unknown"`
- Convert deal values to numeric using `pandas.to_numeric`
- Normalize sector names
- Convert closure probability text values into numeric scores
- Merge data from multiple boards into a unified dataset

This ensures the system remains robust even when working with incomplete or inconsistent records.

---

# 5. Query Understanding Approach

Founder-level questions can be phrased in many ways, making rule-based parsing unreliable.

To address this, the system uses an **LLM (Llama 3 via Groq API)** to classify queries into predefined analytical actions.

Example mapping:

| User Question | Action |
|---------------|--------|
| "show top deals" | `top_deals` |
| "pipeline by sector" | `sector_pipeline` |
| "sector distribution of deals" | `sector_pipeline` |

The LLM converts natural language into structured commands that trigger specific Python analytics functions.

This allows flexible query phrasing without complex rule engineering.

---

# 6. Business Intelligence Layer

Once the intent is detected, Python functions perform structured analysis on the cleaned dataset.

Key analytics implemented include:

### Pipeline by Sector
Counts the number of deals grouped by industry sector.

### Top Deals
Identifies the highest-value deals currently in the pipeline.

### Pipeline Value by Sector
Calculates the total deal value aggregated by sector.

### Pipeline Funnel
Shows distribution of deals across pipeline stages.

These analytics represent the types of insights typically required by leadership teams.

---

# 7. Insight Generation

After analytics are computed, the results are summarized and passed to the LLM to generate **natural-language business insights**.

Example:

Input:  
Top deals table

LLM Output:  
"The pipeline is currently dominated by infrastructure and energy deals, indicating strong sectoral demand."

This step converts raw numerical analysis into **clear executive-level insights**.

---

# 8. User Interface Design

The interface was built using **Streamlit** due to its ability to quickly build interactive data applications.

Advantages of Streamlit:

- rapid development
- interactive UI components
- easy integration with Python data libraries
- straightforward deployment

Key interface features include:

- conversational query input
- structured data tables
- automatic visualizations
- AI-generated insight summaries

---

# 9. Deployment Strategy

The application was deployed using **Streamlit Community Cloud**.

Reasons for choosing Streamlit Cloud:

- simple deployment process
- GitHub integration
- automatic updates on code push
- secure secrets management

API credentials are stored using:
st.secrets["GROQ_API_KEY"]
st.secrets["MONDAY_API_KEY"]


This ensures that sensitive credentials are not exposed in the repository.

---

# 10. Tradeoffs and Limitations

Several tradeoffs were made due to time constraints.

### Limited query scope
The agent currently supports a defined set of analytics actions.

### No conversational memory
Follow-up questions referencing previous responses are not yet supported.

### Basic visualizations
Charts are generated using Streamlit's built-in tools rather than advanced BI frameworks.

These decisions were made to ensure stability and correctness within the project timeline.

---

# 11. Future Improvements

With additional development time, the system could be expanded with:

### Conversational context
Enable follow-up questions referencing previous responses.

### Predictive analytics
Add forecasting capabilities for pipeline revenue.

### Advanced visual dashboards
Implement more interactive visualizations.

### Automated leadership reports
Generate executive summaries for weekly leadership updates.

---

# Conclusion

The final system demonstrates how **AI agents can be combined with live operational data to deliver business intelligence insights**.

By combining:

- LLM-based query understanding
- real-time monday.com data integration
- deterministic analytics
- conversational outputs

the agent provides a scalable foundation for **AI-powered decision support systems**.
