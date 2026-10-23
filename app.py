from datetime import datetime, date
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="StockPilot Pro | Sales & Inventory Intelligence",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA = Path(__file__).parent / "data"

# ---------------------------------------------------------
# DESIGN SYSTEM & STYLING (MIDNIGHT SLATE THEME)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap');

    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --primary-light: #1e2235;
        --primary-subtle: #161b2e;
        --page: #0b0f17;
        --surface: #141c2e;
        --surface-hover: #1a243d;
        --ink: #f8fafc;
        --muted: #94a3b8;
        --line: #1e293b;
        --accent-blue: #3b82f6;
        --accent-emerald: #10b981;
        --accent-amber: #f59e0b;
        --accent-rose: #f43f5e;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: var(--page);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(11, 15, 23, 0.85);
        backdrop-filter: blur(12px);
    }

    [data-testid="stSidebar"] {
        background: var(--surface);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.2rem;
    }

    /* Brand Header */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0 0 1.2rem 0;
        border-bottom: 1px solid var(--line);
        margin-bottom: 1.2rem;
    }

    .brand-mark {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        color: white;
        background: linear-gradient(135deg, #6366f1 0%, #312e81 100%);
        font-size: 19px;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }

    .brand-name {
        font-size: 18px;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: var(--ink);
        line-height: 1.2;
    }

    .brand-caption {
        color: var(--muted);
        font-size: 11px;
        font-weight: 500;
    }

    /* Top Page Header */
    .page-heading {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0.2rem 0 1.4rem 0;
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--line);
    }

    .eyebrow {
        color: #818cf8;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .page-title {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -1px;
        color: var(--ink);
        margin: 0;
    }

    .page-subtitle {
        color: var(--muted);
        font-size: 13px;
        margin-top: 4px;
    }

    /* Metric Cards */
    [data-testid="stMetric"] {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 16px 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -1px rgba(0, 0, 0, 0.1);
        transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
    }

    [data-testid="stMetric"]:hover {
        border-color: var(--primary);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.15);
    }

    [data-testid="stMetricLabel"] p {
        font-size: 11px !important;
        color: var(--muted) !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 21px !important;
        font-weight: 700;
        color: var(--ink);
    }

    /* Custom Sections */
    .section-heading {
        font-size: 16px;
        font-weight: 700;
        letter-spacing: -0.3px;
        color: var(--ink);
        margin: 0 0 2px 0;
    }

    .section-caption {
        font-size: 12px;
        color: var(--muted);
        margin-bottom: 0.8rem;
    }

    /* Buttons */
    .stButton > button, .stDownloadButton > button {
        background: var(--primary);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 13px;
        padding: 0.5rem 1rem;
        transition: all 150ms ease;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: var(--primary-dark);
        color: white;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--line);
        padding-bottom: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 38px;
        border-radius: 6px;
        padding: 0 16px;
        font-weight: 600;
        font-size: 13px;
        color: var(--muted);
        background-color: transparent;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--primary-subtle) !important;
        color: #a5b4fc !important;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }

    .footer {
        border-top: 1px solid var(--line);
        margin-top: 3rem;
        padding: 1.2rem 0;
        color: var(--muted);
        font-size: 12px;
        display: flex;
        justify-content: space-between;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# DATA LOADING & CACHING
# ---------------------------------------------------------
@st.cache_data
def load_sample():
    sales = pd.read_csv(DATA / "sample_sales.csv")
    stock = pd.read_csv(DATA / "sample_stock.csv")
    return sales, stock

def normalise_columns(df):
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    return df

def validate_sales(df):
    required = {"date", "product_id", "product_name", "quantity", "unit_price"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError("Sales file is missing columns: " + ", ".join(sorted(missing)))
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    bad = df[df["quantity"].isna() | df["unit_price"].isna()]
    clean = df.dropna(subset=["quantity", "unit_price"]).copy()
    clean["revenue"] = clean["quantity"] * clean["unit_price"]
    return clean, len(bad)

def validate_stock(df):
    required = {"product_id", "product_name", "stock_quantity", "reorder_level"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError("Stock file is missing columns: " + ", ".join(sorted(missing)))
    df["stock_quantity"] = pd.to_numeric(df["stock_quantity"], errors="coerce")
    df["reorder_level"] = pd.to_numeric(df["reorder_level"], errors="coerce")
    bad = df[df["stock_quantity"].isna() | df["reorder_level"].isna()]
    clean = df.dropna(subset=["stock_quantity", "reorder_level"]).copy()
    clean["status"] = clean.apply(
        lambda r: "Reorder" if r["stock_quantity"] <= r["reorder_level"] else "OK", axis=1
    )
    return clean, len(bad)

# ---------------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">SP</div>
            <div>
                <div class="brand-name">StockPilot Pro</div>
                <div class="brand-caption">Inventory & Sales Intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Data Source")
    source = st.radio(
        "Choose data source",
        ["Use sample data", "Upload CSV files"],
        label_visibility="collapsed",
    )

    if source == "Upload CSV files":
        sales_file = st.sidebar.file_uploader("Sales CSV", type=["csv"])
        stock_file = st.sidebar.file_uploader("Stock CSV", type=["csv"])
        if sales_file is not None and stock_file is not None:
            try:
                sales_raw = normalise_columns(pd.read_csv(sales_file))
                stock_raw = normalise_columns(pd.read_csv(stock_file))
            except Exception as exc:
                st.error(f"Could not read CSV: {exc}")
                st.stop()
        else:
            st.info("Upload both CSV files to continue. Or select sample data.")
            st.stop()
    else:
        sample_sales_path = DATA / "sample_sales.csv"
        sample_stock_path = DATA / "sample_stock.csv"
        if sample_sales_path.exists() and sample_stock_path.exists():
            try:
                sales_raw, stock_raw = load_sample()
            except Exception:
                st.error("Could not load sample data files from data directory.")
                st.stop()
        else:
            st.error("Sample data files not found in 'data/' directory.")
            st.stop()
        sales_raw = normalise_columns(sales_raw)
        stock_raw = normalise_columns(stock_raw)

# Process Data safely
try:
    sales, invalid_sales = validate_sales(sales_raw)
    stock, invalid_stock = validate_stock(stock_raw)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

if sales.empty:
    st.error("No valid sales rows found.")
    st.stop()

sales["date"] = pd.to_datetime(sales["date"], errors="coerce")

# Sidebar Date Filter
with st.sidebar:
    st.divider()
    st.markdown("#### Reporting Period")
    min_date = sales["date"].min().date()
    max_date = sales["date"].max().date()

    date_range = st.date_input(
        "Filter Sales Period",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
        begin = pd.Timestamp(date_range[0])
        finish = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1) - pd.Timedelta(microseconds=1)
        sales = sales[sales["date"].between(begin, finish)].copy()

# ---------------------------------------------------------
# HEADER DISPLAY
# ---------------------------------------------------------
st.markdown(
    """
    <div class="page-heading">
        <div>
            <div class="eyebrow">Operations Intelligence Workspace</div>
            <h1 class="page-title">Sales & Inventory Analytics</h1>
            <div class="page-subtitle">Real-time stock monitoring, revenue trends, and automated inventory replenishment tracking.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# COMPUTATIONS & METRICS
# ---------------------------------------------------------
product_sales = sales.groupby(["product_id", "product_name"], as_index=False).agg(
    units_sold=("quantity", "sum"), revenue=("revenue", "sum")
).sort_values("revenue", ascending=False)

total_revenue = float(sales["revenue"].sum())
total_units = float(sales["quantity"].sum())
low_stock = stock[stock["status"] == "Reorder"]

# Calculate Inventory Asset Value (Stock Quantity * Average Unit Price from Sales or Stock)
avg_prices = sales.groupby("product_id")["unit_price"].mean().reset_index()
stock_valuation = stock.merge(avg_prices, on="product_id", how="left")
stock_valuation["unit_price"] = stock_valuation["unit_price"].fillna(0)
total_inventory_value = (stock_valuation["stock_quantity"] * stock_valuation["unit_price"]).sum()

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Gross Revenue", f"KSh {total_revenue:,.2f}")
m2.metric("Inventory Asset Value", f"KSh {total_inventory_value:,.2f}")
m3.metric("Units Sold", f"{total_units:,.0f}")
m4.metric("Active SKUs", f"{stock['product_id'].nunique():,}")
m5.metric("Low-Stock Alerts", f"{len(low_stock):,}", delta=f"{len(low_stock)} items" if len(low_stock)>0 else "Optimal", delta_color="inverse" if len(low_stock)>0 else "normal")

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# WORKSPACE TABS
# ---------------------------------------------------------
tab_dash, tab_inventory, tab_sales, tab_audit = st.tabs([
    "📊 Executive Dashboard", 
    "📦 Inventory & Restock Plan", 
    "📈 Sales Performance", 
    "📑 Data Quality Audit"
])

# ---------------------------------------------------------
# TAB 1: EXECUTIVE DASHBOARD
# ---------------------------------------------------------
with tab_dash:
    col_left, col_right = st.columns([1.3, 1], gap="medium")

    with col_left:
        st.markdown('<div class="section-heading">Daily Revenue Momentum</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Track daily cash inflows and sales velocity over time.</div>', unsafe_allow_html=True)
        
        daily_trend = sales.groupby(sales["date"].dt.date)["revenue"].sum().reset_index()
        if not daily_trend.empty:
            fig_daily = px.line(
                daily_trend,
                x="date",
                y="revenue",
                markers=True,
                labels={"revenue": "Revenue (KSh)", "date": "Date"},
                color_discrete_sequence=["#6366f1"]
            )
            fig_daily.update_layout(
                template="plotly_dark",
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=310,
            )
            st.plotly_chart(fig_daily, use_container_width=True)
        else:
            st.info("No data available for the selected timeframe.")

    with col_right:
        st.markdown('<div class="section-heading">Revenue Share by Top Products</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Top revenue-generating catalog items.</div>', unsafe_allow_html=True)

        if not product_sales.empty:
            top_products = product_sales.head(6)
            fig_bar = px.bar(
                top_products,
                x="revenue",
                y="product_name",
                orientation="h",
                labels={"revenue": "Revenue (KSh)", "product_name": "Product"},
                color="revenue",
                color_continuous_scale="Purples"
            )
            fig_bar.update_layout(
                template="plotly_dark",
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=310,
                yaxis=dict(autorange="reversed")
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("No sales breakdown available.")

# ---------------------------------------------------------
# TAB 2: INVENTORY & RESTOCK PLAN
# ---------------------------------------------------------
with tab_inventory:
    st.markdown('<div class="section-heading">Inventory Status & Restock Requirements</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Identify items nearing depletion and calculate restock priorities.</div>', unsafe_allow_html=True)

    inv_report = stock.merge(avg_prices, on="product_id", how="left")
    inv_report["unit_price"] = inv_report["unit_price"].fillna(0)
    inv_report["deficit"] = inv_report.apply(
        lambda r: max(0, r["reorder_level"] - r["stock_quantity"]), axis=1
    )
    inv_report["estimated_restock_cost"] = inv_report["deficit"] * inv_report["unit_price"]

    st.dataframe(
        inv_report[["product_id", "product_name", "stock_quantity", "reorder_level", "status", "estimated_restock_cost"]],
        use_container_width=True,
        hide_index=True,
        column_config={
            "estimated_restock_cost": st.column_config.NumberColumn("Est. Restock Cost (KSh)", format="KSh %.2f"),
            "stock_quantity": "Current Stock",
            "reorder_level": "Reorder Level",
            "status": "Stock Status"
        }
    )

    total_restock_expenditure = inv_report["estimated_restock_cost"].sum()
    st.markdown(f"### Total Estimated Restock Capital Required: `KSh {total_restock_expenditure:,.2f}`")

# ---------------------------------------------------------
# TAB 3: SALES PERFORMANCE
# ---------------------------------------------------------
with tab_sales:
    st.markdown('<div class="section-heading">Detailed Product Sales Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Comprehensive catalog performance metrics.</div>', unsafe_allow_html=True)

    st.dataframe(
        product_sales,
        use_container_width=True,
        hide_index=True,
        column_config={
            "revenue": st.column_config.NumberColumn("Total Revenue (KSh)", format="KSh %.2f"),
            "units_sold": st.column_config.NumberColumn("Units Sold", format="%.,0f")
        }
    )

    report = product_sales.merge(
        stock[["product_id", "stock_quantity", "reorder_level", "status"]],
        on="product_id", how="left"
    )
    report_csv = report.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Comprehensive Report (CSV)",
        data=report_csv,
        file_name="stockpilot_executive_report.csv",
        mime="text/csv"
    )

# ---------------------------------------------------------
# TAB 4: DATA QUALITY AUDIT
# ---------------------------------------------------------
with tab_audit:
    st.markdown('<div class="section-heading">Data Hygiene & Validation Audit</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Inspect anomalies, missing entries, and excluded data rows.</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.metric("Excluded Sales Records", f"{invalid_sales:,}")
    c2.metric("Excluded Stock Records", f"{invalid_stock:,}")

    if invalid_sales > 0 or invalid_stock > 0:
        st.warning("⚠️ **Data Quality Notice:** Rows with missing timestamps or invalid numeric pricing/quantities were filtered out during validation to preserve reporting accuracy.")
    else:
        st.success("✅ Perfect data hygiene: All uploaded records passed structural and type validation successfully.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <div>StockPilot Pro · Sales & Inventory Intelligence</div>
        <div>Prototype Demo · For evaluation purposes only</div>
    </div>
    """,
    unsafe_allow_html=True,
)