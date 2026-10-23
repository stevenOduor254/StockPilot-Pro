# 📦 StockPilot Pro

> **Executive-Grade Sales Analytics & Inventory Intelligence Workspace**

StockPilot Pro is a modern, high-performance web dashboard built with **Python**, **Streamlit**, and **Plotly**. Designed for retail managers, warehouse operators, and financial analysts, it transforms raw sales ledgers and stock logs into actionable operational insights—including automated stock alert tracking, daily revenue trend analysis, asset valuation, and restock cost estimations.

---

## ✨ Key Features

* **📊 Executive Dashboard:** Real-time visibility into Gross Revenue, Inventory Asset Value, Units Sold, Active SKUs, and Low-Stock Alert counts.
* **📈 Sales Velocity Trends:** Interactive time-series charts visualizing daily cash inflows and identifying sales momentum peaks.
* **📦 Inventory Asset Valuation:** Automatically computes capital bound in current warehouse stock using real-time inventory counts and average selling prices.
* **🚨 Automated Restock & Deficit Estimator:** Detects items falling below safety reorder thresholds and calculates the exact capital required to replenish inventory levels.
* **📑 Multi-Tab Workspace Architecture:** Clean separation into *Executive Dashboard*, *Inventory & Restock Plan*, *Sales Performance*, and *Data Quality Audit*.
* **🛡️ Built-in Data Hygiene Audit:** Ingests CSV uploads and automatically isolates malformed rows or missing data types without crashing reporting pipelines.
* **🎨 Modern Midnight Slate Theme:** Premium, high-contrast dark theme built with `Plus Jakarta Sans` typography and `JetBrains Mono` numerical styling.

---

## 🛠️ Repository Structure

```text
.
├── app.py                      # Main Streamlit dashboard application
├── requirements.txt            # Python dependencies
├── data/
│   ├── sample_sales.csv        # Pre-loaded sample sales records
│   └── sample_stock.csv        # Pre-loaded sample inventory stock records
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have **Python 3.9+** installed on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/stockpilot-pro.git
cd stockpilot-pro
```

### 3. Set Up a Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

*(Or install manually: `pip install streamlit pandas numpy plotly`)*

### 5. Launch the Application

```bash
streamlit run app.py
```

The app will launch automatically in your web browser at `http://localhost:8501`.

---

## 📋 CSV Data Schema Requirements

If you upload custom datasets using the sidebar CSV uploader, ensure your files follow these column header structures:

### 1. Sales Dataset (`sales.csv`)

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `date` | Date | Date of transaction (`YYYY-MM-DD`) | `2026-03-15` |
| `product_id` | String | Unique product identifier/SKU | `SKU-1002` |
| `product_name` | String | Name or description of the product | `Wireless Mouse` |
| `quantity` | Integer | Units sold | `4` |
| `unit_price` | Float | Unit selling price | `2500.00` |

### 2. Inventory Stock Dataset (`stock.csv`)

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `product_id` | String | Unique product identifier/SKU | `SKU-1002` |
| `product_name` | String | Name or description of the product | `Wireless Mouse` |
| `stock_quantity` | Integer | Units currently remaining in warehouse stock | `12` |
| `reorder_level` | Integer | Minimum threshold before triggering reorder alert | `15` |

---

## 📖 How to Use

1. **Select Data Source (Sidebar):**
   * **Use Sample Data:** Instantly test the application using pre-loaded sales and stock files.
   * **Upload CSV Files:** Upload your custom `Sales CSV` and `Stock CSV` files.

2. **Filter Operational Date Ranges:**
   * Adjust the date range picker in the sidebar to restrict revenue trend analysis and unit summaries to specific reporting windows.

3. **Navigate Workspace Tabs:**
   * **Executive Dashboard:** Monitor core operational KPIs and revenue distribution charts.
   * **Inventory & Restock Plan:** Review low-stock warnings and total estimated restock capital required.
   * **Sales Performance:** Analyze detailed SKU sales totals and export compiled reports directly to CSV.
   * **Data Quality Audit:** Check rows filtered out due to formatting errors or missing values.

---

## 🤝 Contributing

Contributions are welcome! To suggest enhancements or report issues:

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add NewFeature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a Pull Request.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more details.
