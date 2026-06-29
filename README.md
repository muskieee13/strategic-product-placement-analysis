# Strategic Product Placement Analysis

> Investigating the relationship between product positioning, sales performance, and consumer behavior using Tableau and Flask.

![Dashboard Screenshot](Screenshot 2026-06-29 122505.png)

---

## 📋 Project Objective

This project investigates the relationship between **product positioning**, **sales performance**, and **consumer behavior**. Using Tableau, we analyze retail sales data to uncover insights into how different positioning strategies impact sales and consumer preferences. By visualizing the data, we provide **actionable recommendations** to optimize product positioning strategies and drive revenue growth.

A retail company wants to understand the impact of product positioning on its sales and consumer behavior. They have collected data on sales figures, product placement, and consumer demographics. Through **data visualization with Tableau** and a **Flask web application**, the company gains actionable insights to improve product positioning strategies and increase revenue.

---

## 🎯 Business Scenarios

### Scenario 1: Film & Television Production Companies
Production companies can utilize strategic product placement analysis to optimize revenue through brand partnerships. By employing Tableau visualization, they can analyze effectiveness of product placements in different scenes/episodes, negotiate better brand deals, and make data-driven placement decisions.

### Scenario 2: Retail & Consumer Goods Companies
Retailers can leverage strategic product placement analysis to enhance marketing strategies and boost sales. Using Tableau, they track product performance across store locations and websites, identify high-traffic areas, understand customer preferences, and optimize placement to drive conversions.

### Scenario 3: Advertising Agencies
Agencies can benefit from strategic product placement analysis to optimize advertising campaigns. They analyze the impact of placements across media channels (movies, TV shows, online videos), demonstrate ROI, refine targeting strategies, and improve campaign effectiveness for clients.

---

## 🔗 Live Tableau Dashboard

👉 **[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/viz/StrategicProductPlacementAnalysis/Dashboard1)**

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Tableau Public** | Data visualization, dashboard & story creation |
| **Python 3.12** | Backend programming & data analysis |
| **Flask** | Web framework for embedding dashboards |
| **Pandas** | Data manipulation & analysis |
| **Matplotlib** | Chart generation |
| **Bootstrap 5** | Responsive frontend UI design |
| **Chart.js** | Interactive client-side charts |
| **HTML / CSS / JS** | Web interface |

---

## 📊 Dataset

| Attribute | Details |
|-----------|---------|
| **Records** | 1,000 retail transactions |
| **Time Period** | January 2023 – January 2024 |
| **Categories** | Electronics, Clothing, Beauty |
| **Features** | Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount |

---

## 📈 Key Performance Indicators

| KPI | Value |
|-----|-------|
| Total Revenue | $456,000 |
| Total Transactions | 1,000 |
| Average Order Value | $456.00 |
| Unique Customers | 1,000 |
| Top Category (Revenue) | Electronics (34.4%) |

---

## 💡 Key Insights & Recommendations

### Insights
1. **Electronics leads in total revenue** ($156,905 — 34.4%) due to premium pricing ($300–$500 per unit).
2. **Clothing dominates transaction volume** (351 transactions) — the most popular category.
3. **Age group 46–55 is the top spending demographic** ($100,690 — 22.1%), followed closely by 26–35.
4. **Gender spending is balanced** — Female 51.1% vs Male 48.9%.
5. **May is the peak sales month** ($53,150), with seasonal peaks in Feb, Oct, and Dec.
6. **$500 price point generates the most revenue** ($247,500 from 199 transactions).

### Recommendations
- **Premium Placement for Electronics**: Prioritize high-visibility placements for electronics products.
- **Volume Strategy for Clothing**: Increase shelf space and online presence for clothing items.
- **Targeted Marketing**: Focus campaigns on the 26–55 age demographic for maximum ROI.
- **Seasonal Campaigns**: Align promotions with May, October, and holiday season peaks.
- **Cross-Category Bundling**: Create product bundles combining high-volume and high-value categories.
- **Price-Point Optimization**: Strategically promote $300–$500 items in premium display areas.

---

## 🌐 Web Application (Flask Integration)

A Flask web application was developed that embeds the Tableau dashboard and story within a responsive, Bootstrap-based web interface.

### Features
- ✅ Interactive Tableau Dashboard (embedded)
- ✅ Tableau Story Visualization (embedded)
- ✅ Real-time KPI cards computed from data
- ✅ Interactive Chart.js visualizations (monthly trend, category pie, gender bar, age group bar)
- ✅ Category performance table
- ✅ Bootstrap 5 responsive UI
- ✅ Navigation between Dashboard, Story, and About pages
- ✅ REST API endpoint (`/api/data`) for raw data access

### How to Run

```bash
# 1. Clone the repository
git clone https://github.com/m4nisharma/strategic-product-placement-analysis.git
cd Strategic-Product-Placement-Analysis

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# 5. Open browser at http://localhost:5000
```

### Run Data Analysis Script
```bash
python data_analysis.py
```

---

## 📁 Project Structure

```
Strategic-Product-Placement-Analysis/
│
├── app.py                          # Flask web application (routes, data processing)
├── data_analysis.py                # Standalone Python data analysis script
├── requirements.txt                # Python dependencies
├── DataAnalyticsproject.twb        # Tableau workbook file
├── README.md                       # Project documentation
│
├── Data/
│   └── retail_sales_dataset 2.csv  # Source dataset (1,000 records)
│
├── Extracts/
│   └── *.hyper                     # Tableau data extract
│
├── static/
│   └── css/
│       └── style.css               # Custom CSS styles (responsive)
│
├── templates/
│   ├── base.html                   # Base template (Jinja2 inheritance)
│   ├── index.html                  # Dashboard page (KPIs + Charts + Tableau)
│   ├── story.html                  # Tableau Story page
│   └── about.html                  # About / documentation page
│
├── Strategic Product Placement Analysis.png  # Dashboard screenshot
└── venv/                           # Virtual environment (not tracked)
```

### File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Flask application with routes for Dashboard, Story, About, and API |
| `data_analysis.py` | Comprehensive Python data analysis with 10 analysis sections |
| `requirements.txt` | Python package dependencies (Flask, Pandas, Matplotlib) |
| `templates/base.html` | Base HTML template with navbar, footer, Bootstrap & Chart.js CDN |
| `templates/index.html` | Dashboard with 6 KPI cards, 4 Chart.js charts, Tableau embed, data table |
| `templates/story.html` | Tableau Story embed with scene descriptions and key takeaways |
| `templates/about.html` | Project documentation, scenarios, architecture, team info |
| `static/css/style.css` | Custom responsive CSS with card styles, chart containers, animations |

---

## 📊 Visualizations Created

| # | Visualization | Type | Tool |
|---|---------------|------|------|
| 1 | Sales Overview Dashboard | Multi-chart Dashboard | Tableau |
| 2 | Product Placement Analysis Story | Story (6 scenes) | Tableau |
| 3 | Monthly Sales Trend | Line Chart (filled) | Chart.js |
| 4 | Sales by Product Category | Doughnut Chart | Chart.js |
| 5 | Sales by Gender | Bar Chart | Chart.js |
| 6 | Sales by Age Group | Bar Chart | Chart.js |
| 7 | Category Performance Table | Data Table | HTML/CSS |
| 8 | KPI Cards | Metric Cards | HTML/CSS/Flask |

---

## ✅ Project Checklist

| Activity | Status |
|----------|--------|
| Data Collection & Extraction from Database | ✅ Complete |
| Connect data with Tableau | ✅ Complete |
| Data Preparation for Visualization | ✅ Complete |
| Unique Visualizations (8+) | ✅ Complete |
| Responsive Dashboard Design | ✅ Complete |
| Story with Multiple Scenes (6) | ✅ Complete |
| Data Filters Utilization | ✅ Complete |
| Calculation Fields | ✅ Complete |
| Web Integration (Flask + Tableau) | ✅ Complete |
| Project Documentation | ✅ Complete |

---

## 👥 Team Members

| Name | Role |
|------|------|
| Muskan S.K| Team Lead |
| Pujitha Leela.K | Member |
| SRI VARSHINI VELAGA | Member |
| Afrin S.K | Member |
| Saniya S.K | Member |

---

## 📝 License

This project was created for academic/educational purposes as part of a Data Analytics course project.
