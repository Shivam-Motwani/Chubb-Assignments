# World Exports & Global Trade Performance Analytics Platform

## 1. Project Overview

This project implements an end-to-end data analytics platform to analyze global export and international trade performance. It is designed to simulate a real-world data engineering and analytics workflow used by international trade organizations and economic research bodies.

The platform automates data ingestion, cleaning, transformation, analytics, and visualization to provide actionable insights into country-wise, region-wise, and product-wise export trends.

---

## 2. Business Problem

Global trade data is often:

* Distributed across multiple raw files
* Manually consolidated, leading to inconsistencies
* Difficult to analyze at country, region, and product levels
* Limited in identifying emerging markets and declining sectors

This project addresses these challenges by building a centralized, automated analytics solution that supports data-driven trade and economic decision-making.

---

## 3. Solution Architecture

The solution follows a **Bronze–Silver–Gold data lake architecture** orchestrated using Apache Airflow and executed on Databricks.

### High-Level Flow

1. Raw export data is ingested into the Bronze layer
2. Data is cleaned and standardized in the Silver layer
3. Aggregated KPIs are generated in the Gold layer
4. Advanced analytics (forecasting and emerging market detection) are performed
5. Final datasets are consumed by Power BI dashboards

---

## 4. Technology Stack

### Data Processing & Analytics

* Python
* Pandas, NumPy
* PySpark
* Databricks

### Workflow Orchestration

* Apache Airflow

### Data Storage

* CSV

### Visualization

* Power BI

### Other Tools

* Git & GitHub
* Jupyter / Databricks Notebooks

---

## 5. Data Architecture (Bronze–Silver–Gold)

### Bronze Layer – Raw Ingestion

* Ingests raw export CSV files
* Performs schema validation
* Handles ingestion errors and logging
* Stores raw data in its original structure

### Silver Layer – Cleaning & Standardization

* Handles missing and inconsistent values
* Standardizes country codes and product categories
* Ensures correct data types
* Produces analytics-ready cleaned datasets

### Gold Layer – Aggregations & KPIs

* Aggregates exports by country, region, year, and product
* Computes key trade metrics and KPIs
* Produces final datasets for reporting and analytics

### Analytics Layer

* Forecasting of export trends
* Identification of emerging export markets
* Detection of declining sectors

---

## 6. Databricks Notebooks

| Notebook            | Purpose                           |
| ------------------- | --------------------------------- |
| 01_capstone_bronze | Raw data ingestion (Bronze layer) |
| 02_capstone_silver  | Data cleaning and standardization |
| 03_capstone_gold        | Aggregations and KPI generation   |
| 04_capstone_forecasting      | Export trend forecasting          |
| 05_capstone_emerging_markets | Emerging market identification    |

Databricks is used to leverage Spark for scalable data processing and analytics.

---

## 7. Airflow Workflow Orchestration

Apache Airflow is used to define and manage the ETL and analytics workflow.

### DAG Overview

* DAG Name: `global_trade_bronze_silver_gold_pipeline`
* Schedule: Daily
* Purpose: Orchestrate Databricks notebooks execution

### Task Flow

```
capstone_bronze → capstone_silver → capstone_gold → capstone_forecasting → capstone_emerging_markets
```

Each Airflow task represents a Databricks job execution. Due to academic environment constraints, Databricks job IDs are used as placeholders to demonstrate orchestration design.

---

## 8. Data Validation & Quality Checks

* Row count reconciliation across layers
* Null and missing value handling verification
* Aggregation accuracy checks
* Year-over-year metric validation
* Power BI dashboard data verification

---

## 9. Visualization & Reporting (Power BI)

Power BI dashboards are built on top of Gold and analytics datasets.

### Dashboards Include:

* Global export performance overview
* Country-wise export comparison
* Product-wise export trends
* Regional trade performance
* Key trade KPIs for policymakers

These dashboards enable interactive analysis and decision support.

---

## 10. Key Business Insights

* Identification of top exporting countries and products
* Detection of high-growth regions
* Recognition of declining trade sectors
* Emerging export market identification
* Forecast-based trade trend insights

---

## 11. Testing & Validation

* ETL pipeline correctness validation
* Airflow DAG execution verification
* Spark transformation validation
* Dashboard accuracy checks

---

## 12. Limitations & Future Enhancements

### Current Limitations

* Batch-based processing only
* Databricks jobs triggered conceptually via Airflow

### Future Scope

* Real-time data ingestion using Kafka
* Direct Airflow–Databricks job integration
* Cloud data warehouse integration
* Advanced ML-based trade forecasting

---

## 13. Conclusion

This project demonstrates a complete, industry-aligned data engineering and analytics solution for global trade analysis. It showcases scalable data processing, workflow orchestration, advanced analytics, and business-focused visualization using modern data engineering tools.
