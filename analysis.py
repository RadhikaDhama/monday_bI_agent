import pandas as pd


def convert_to_dataframe(api_response):
    """
    Convert monday.com API response into a pandas DataFrame.
    """

    boards = api_response.get("data", {}).get("boards", [])

    if not boards:
        print("No boards found in API response")
        return pd.DataFrame()

    board = boards[0]

    # Support both API formats
    if "items_page" in board:
        items = board["items_page"].get("items", [])
    else:
        items = board.get("items", [])

    if not items:
        print("No items found in board")
        return pd.DataFrame()

    rows = []

    for item in items:

        row = {"Deal Name": item.get("name", "Unknown")}

        for column in item.get("column_values", []):
            title = column.get("column", {}).get("title", "Unknown")
            value = column.get("text")

            row[title] = value

        rows.append(row)

    df = pd.DataFrame(rows)

    print("Converted dataframe shape:", df.shape)

    return df

def clean_data(df):
    """
    Clean and normalize monday.com board data to ensure reliable analysis.

    Cleaning steps:
    - Handle missing values
    - Normalize sector names
    - Convert deal values to numeric
    - Convert closure probability to numeric score
    """

    if df.empty:
        return df

    # Handle missing values
    df.fillna("Unknown", inplace=True)

    # Normalize sector names
    if "Sector/service" in df.columns:

        df["Sector/service"] = df["Sector/service"].str.strip()

        sector_map = {
            "Renewabl": "Renewable",
            "Constructi": "Construction",
            "DSP": "Defense"
        }

        df["Sector/service"] = df["Sector/service"].replace(sector_map)

    # Convert deal values to numeric
    if "Masked Deal value" in df.columns:

        df["Masked Deal value"] = pd.to_numeric(
            df["Masked Deal value"],
            errors="coerce"
        )

        df["Masked Deal value"].fillna(0, inplace=True)

    # Convert probability text to numeric score
    if "Closure Probability" in df.columns:

        prob_map = {
            "High": 0.8,
            "Medium": 0.5,
            "Low": 0.2
        }

        df["Probability Score"] = df["Closure Probability"].map(prob_map)

    return df


def pipeline_by_sector(df):
    """
    Count number of deals by sector.
    """

    sector_col = None

    for col in df.columns:
        if "sector" in col.lower():
            sector_col = col
            break

    if sector_col is None:
        return pd.Series(dtype="int64")

    return df.groupby(sector_col).size().sort_values(ascending=False)


def pipeline_value_by_sector(df):
    """
    Calculate total pipeline value grouped by sector.
    """

    if "Sector/service" not in df.columns or "Masked Deal value" not in df.columns:
        return pd.Series(dtype="float64")

    return (
        df.groupby("Sector/service")["Masked Deal value"]
        .sum()
        .sort_values(ascending=False)
    )


def top_deals(df, n=5):
    """
    Return top N deals by deal value.
    """

    if "Masked Deal value" not in df.columns:
        return pd.DataFrame()

    columns_to_show = [
        col for col in ["Deal Name", "Masked Deal value", "Sector/service"]
        if col in df.columns
    ]

    df_sorted = df.sort_values(by="Masked Deal value", ascending=False)

    return df_sorted[columns_to_show].head(n)


def expected_pipeline_value(df):
    """
    Calculate expected pipeline value using probability weighting.
    """

    if "Masked Deal value" not in df.columns:
        return 0

    if "Probability Score" not in df.columns:
        return df["Masked Deal value"].sum()

    weighted_value = (
        df["Masked Deal value"] * df["Probability Score"]
    )

    return weighted_value.sum()


def deals_by_stage(df):
    """
    Show distribution of deals across pipeline stages.
    """

    if "Deal Stage" not in df.columns:
        return pd.Series(dtype="int64")

    return df["Deal Stage"].value_counts()


def top_clients(df, n=5):
    """
    Identify clients with the highest number of deals.
    """

    if "Client Code" not in df.columns:
        return pd.Series(dtype="int64")

    return df["Client Code"].value_counts().head(n)


def data_quality_report(df):
    """
    Generate a simple data quality summary.
    """

    report = {
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Deals": int(
            df["Deal Name"].duplicated().sum()
        ) if "Deal Name" in df.columns else 0
    }

    return report