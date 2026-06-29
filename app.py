"""
Strategic Product Placement Analysis - Flask Web Application
=============================================================
This Flask application serves as the web interface for the Strategic Product 
Placement Analysis project. It embeds Tableau dashboards and stories, and 
provides data-driven insights from retail sales data.
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "Data", "retail_sales_dataset 2.csv")

TABLEAU_DASHBOARD_URL = (
    "https://public.tableau.com/views/DataAnalyticsproject_17721267059890/"
    "StrategicProductPlacementAnalysis"
)
TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/DataAnalyticsproject_17721267059890/"
    "Story1"
)


def load_data():
    """Load and return the retail sales DataFrame."""
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def compute_kpis(df):
    """Return a dict of key performance indicators."""
    return {
        "total_revenue": f"${df['Total Amount'].sum():,.0f}",
        "total_transactions": f"{len(df):,}",
        "avg_order_value": f"${df['Total Amount'].mean():,.2f}",
        "unique_customers": f"{df['Customer ID'].nunique():,}",
        "top_category": df.groupby("Product Category")["Total Amount"]
        .sum()
        .idxmax(),
        "avg_quantity": f"{df['Quantity'].mean():.1f}",
    }


def compute_category_stats(df):
    """Return per-category aggregated stats."""
    stats = (
        df.groupby("Product Category")
        .agg(
            total_sales=("Total Amount", "sum"),
            avg_sales=("Total Amount", "mean"),
            total_qty=("Quantity", "sum"),
            transaction_count=("Transaction ID", "count"),
        )
        .reset_index()
    )
    stats = stats.sort_values("total_sales", ascending=False)
    return stats.to_dict(orient="records")


def compute_gender_stats(df):
    """Return per-gender aggregated stats."""
    stats = (
        df.groupby("Gender")
        .agg(
            total_sales=("Total Amount", "sum"),
            avg_sales=("Total Amount", "mean"),
            transaction_count=("Transaction ID", "count"),
        )
        .reset_index()
    )
    return stats.to_dict(orient="records")


def compute_monthly_trend(df):
    """Return monthly sales trend."""
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    trend = df.groupby("Month")["Total Amount"].sum().reset_index()
    return trend.to_dict(orient="records")


def compute_age_groups(df):
    """Return sales by age group."""
    bins = [0, 25, 35, 45, 55, 100]
    labels = ["18-25", "26-35", "36-45", "46-55", "55+"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)
    stats = (
        df.groupby("Age Group", observed=True)
        .agg(total_sales=("Total Amount", "sum"), count=("Transaction ID", "count"))
        .reset_index()
    )
    stats["Age Group"] = stats["Age Group"].astype(str)
    return stats.to_dict(orient="records")


# ─── Routes ──────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    """Dashboard page with embedded Tableau dashboard."""
    df = load_data()
    kpis = compute_kpis(df)
    category_stats = compute_category_stats(df)
    gender_stats = compute_gender_stats(df)
    monthly_trend = compute_monthly_trend(df)
    age_groups = compute_age_groups(df)
    return render_template(
        "index.html",
        kpis=kpis,
        category_stats=category_stats,
        gender_stats=gender_stats,
        monthly_trend=monthly_trend,
        age_groups=age_groups,
        tableau_url=TABLEAU_DASHBOARD_URL,
    )


@app.route("/story")
def story():
    """Tableau Story visualization page."""
    return render_template("story.html", tableau_url=TABLEAU_STORY_URL)


@app.route("/about")
def about():
    """Project description and documentation page."""
    return render_template("about.html")


@app.route("/api/data")
def api_data():
    """REST endpoint returning the raw dataset as JSON."""
    df = load_data()
    return jsonify(df.to_dict(orient="records"))


# ─── Main ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
