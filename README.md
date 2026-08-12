# 🏭 Factory Reallocation & Shipping Optimization System

### 📦 Nassau Candy Distributor

An interactive data-driven dashboard developed to analyze sales, profitability, lead time, shipping performance, operational risk, factory performance, and potential factory reallocation opportunities for Nassau Candy Distributor.

The system combines data analysis, interactive visualization, and historical factory-level benchmarks to support better operational and shipping decisions.

---

## 📌 Project Overview

Factory allocation and shipping decisions can have a direct impact on delivery time, operational risk, profitability, and overall shipping efficiency.

This project provides an interactive platform where users can analyze historical order data, identify operational problem areas, and evaluate potential factory reallocation scenarios.

The Streamlit dashboard allows users to filter the data, monitor key performance indicators, analyze factory and shipping performance, and evaluate whether moving orders from one factory to another may provide an improvement.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze overall sales and profitability performance.
- Monitor factory-wise performance.
- Identify high-risk orders.
- Identify slow-shipping orders.
- Analyze average lead time across factories.
- Analyze shipping performance by shipping mode.
- Compare factory performance using historical data.
- Identify potential factory reallocation opportunities.
- Evaluate the impact of a potential factory reassignment.
- Support data-driven operational decision-making.
- Provide an interactive and user-friendly dashboard for analysis.

---

## 🚀 Key Features

### 📊 Key Performance Indicators

The dashboard provides important high-level KPIs:

- Total Orders
- Total Sales
- Total Profit
- Average Lead Time

These KPIs provide an immediate overview of the current filtered dataset.

---

### 📌 Key Insights

The dashboard automatically generates concise insights based on the currently selected filters.

The insights include:

- Highest sales-performing region
- Highest gross profit-performing factory
- Factory with the highest average lead time
- Slow-shipping and high-risk order counts

This helps users understand the most important findings without having to interpret every chart manually.

---

### 📈 Sales & Profit Analysis

The dashboard provides visual analysis of:

- Sales by Region
- Gross Profit by Factory
- Sales by Ship Mode
- Risk Level Distribution
- Recommendation Status
- Average Lead Time by Factory

These visualizations help identify differences in regional sales, factory profitability, shipping behavior, operational risk, and lead-time performance.

---

### 🎯 Optimization Recommendation

The dashboard identifies operational areas that require attention by monitoring:

- High-risk orders
- Slow-shipping orders
- Average lead time

The recommendation section highlights orders that may require further review for possible factory reallocation and shipping optimization.

---

### 🔄 Factory Reallocation Scenario

One of the main decision-support features of the dashboard is the Factory Reallocation Scenario.

Users can compare:

**Current Factory → Potential New Factory**

The scenario evaluates historical factory-level benchmarks and displays:

- Current Orders
- Lead Time Change
- Margin Change
- Target Factory
- Overall scenario recommendation

If the selected factory does not provide a clear improvement, the system displays:

> No Clear Improvement

This prevents unnecessary factory reallocation when the historical benchmark does not indicate a meaningful benefit.

---

### 🔍 Interactive Dashboard Filters

Users can dynamically filter the dashboard using:

- Region
- Factory
- Ship Mode
- Order Year

All major dashboard metrics, insights, charts, and analysis respond to the selected filters.

---

### 📋 Filtered Dataset

Users can:

- View the filtered dataset directly in the dashboard.
- Download the filtered dataset as a CSV file.

This makes the dashboard useful not only for visualization but also for further analysis.

---

## 🛠️ Technologies Used

### Python
Used as the primary programming language for data processing and dashboard development.

### Streamlit
Used to build the interactive web-based dashboard.

### Pandas
Used for data loading, filtering, grouping, aggregation, and analysis.

### Plotly
Used to create interactive charts and visualizations.

### Machine Learning
Used as part of the broader project objective for data-driven shipping and factory optimization.

### Power BI
Used for additional business intelligence and dashboard analysis during the project.

### Microsoft Excel
Used for dataset preparation, cleaning, transformation, and validation.

---

## 📁 Project Structure

```text
Factory-Reallocation-Shipping-Optimization/
│
├── app.py
├── Final_Nassau_Candy_Predictions.xlsx
├── README.md
├── requirements.txt
├── .gitignore

> The exact folder structure may vary depending on the files required by the Streamlit application.

---

## 📊 Dashboard Flow

```text
Dashboard Overview
        ↓
Key Performance Indicators
        ↓
Key Insights
        ↓
Sales & Profit Analysis
        ↓
Optimization Recommendation
        ↓
Factory Reallocation Scenario
        ↓
Filtered Dataset
        ↓
Download Filtered Data
```

---

## 🔄 Decision-Support Workflow

```text
Historical Order Data
        ↓
Data Cleaning & Preparation
        ↓
Interactive Filtering
        ↓
Performance Analysis
        ↓
Risk & Shipping Analysis
        ↓
Factory Performance Comparison
        ↓
Reallocation Scenario Evaluation
        ↓
Optimization Recommendation
```

---

## 📌 Example Scenario

The Factory Reallocation Scenario compares the current factory with a potential target factory.

For example:

```text
Current Factory
      ↓
Potential New Factory
      ↓
Compare Historical Performance
      ↓
Lead Time Change
      ↓
Margin Change
      ↓
Recommendation
```

If the potential factory does not provide sufficient improvement, the system can return:

**No Clear Improvement**

This ensures that reallocation decisions are evaluated rather than automatically recommended.

---

## 💡 Business Value

The project helps transform historical order data into actionable operational information.

It can help users:

- Identify operational bottlenecks.
- Monitor shipping performance.
- Identify high-risk orders.
- Compare factory performance.
- Understand profitability patterns.
- Detect potential reallocation opportunities.
- Evaluate possible operational improvements.
- Make more informed factory and shipping decisions.

---

## 📈 Dashboard Highlights

The final dashboard includes:

- 📦 Order volume monitoring
- 💰 Sales analysis
- 📈 Profit analysis
- ⏱️ Lead-time monitoring
- 🚚 Shipping analysis
- ⚠️ Risk analysis
- 🏭 Factory performance analysis
- 🎯 Optimization recommendations
- 🔄 Factory reallocation scenarios
- 🔍 Interactive filtering
- 📋 Filtered data viewing
- 📥 CSV data download

---

## 🔮 Future Scope

The system can be further enhanced with:

- Real-time shipping data integration.
- Automated factory allocation recommendations.
- More advanced predictive models.
- Cost and distance optimization.
- Delivery-time prediction.
- Automated alerts for high-risk orders.
- Optimization based on multiple business constraints.
- Integration with live operational systems.

---

## 👩‍💻 Developer

**Manya**

B.Tech IT | GJUST

**B.Tech IT Internship Project**

---

## 📄 Project Type

**Data Analytics • Business Intelligence • Streamlit Dashboard • Factory Optimization • Shipping Analysis**

---
