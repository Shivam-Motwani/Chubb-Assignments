# World Exports & Global Trade Performance Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0%2B-red.svg)](https://airflow.apache.org/)
[![Databricks](https://img.shields.io/badge/Databricks-Enabled-orange.svg)](https://databricks.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Ready-yellow.svg)](https://powerbi.microsoft.com/)

> An end-to-end data analytics platform for analyzing global export and international trade performance, built with modern data engineering best practices.

---

## Table of Contents

- [Project Overview](#1-project-overview)
- [Business Problem](#2-business-problem)
- [Solution Architecture](#3-solution-architecture)
- [Technology Stack](#4-technology-stack)
- [Data Architecture](#5-data-architecture-bronzeservergold)
- [Databricks Notebooks](#6-databricks-notebooks)
- [Airflow Orchestration](#7-airflow-workflow-orchestration)
- [Data Validation](#8-data-validation--quality-checks)
- [Visualization](#9-visualization--reporting-power-bi)
- [Business Insights](#10-key-business-insights)
- [Testing](#11-testing--validation)
- [Limitations & Future Work](#12-limitations--future-enhancements)
- [Repository Structure](#13-repository-structure)
- [Getting Started](#14-getting-started)
- [Acknowledgements](#15-acknowledgements)

---

## 1. Project Overview

This project implements an end-to-end data analytics platform to analyze global export and international trade performance. It simulates real-world data engineering workflows used by international trade organizations and economic research bodies.

The platform automates data ingestion, cleaning, transformation, analytics, and visualization, providing actionable insights into country-wise, region-wise, and product-wise export trends.

### Key Features

- **Automated ETL Pipeline** - Complete data pipeline from raw ingestion to analytics
- **Medallion Architecture** - Bronze-Silver-Gold data lake implementation
- **Workflow Orchestration** - Apache Airflow for reliable job scheduling
- **Advanced Analytics** - Export forecasting and emerging market detection
- **Interactive Dashboards** - Power BI visualizations for business insights
- **Data Quality Checks** - Comprehensive validation at every layer

---

## 2. Business Problem

### Challenges

Global trade data is often:

- **Distributed** across multiple raw files
- **Manually consolidated**, leading to inconsistencies
- **Difficult to analyze** at country, region, and product levels
- **Limited insights** for identifying emerging markets and declining sectors

### Solution

This project addresses these challenges by building a centralized, automated analytics solution that supports data-driven trade and economic decision-making.

---

## 3. Solution Architecture

The solution follows a **Bronze–Silver–Gold** data lake architecture orchestrated using **Apache Airflow** and executed on **Databricks**.

### High-Level Flow

```mermaid
graph LR
    A[Raw CSV Files] --> B[Bronze Layer]
    B --> C[Silver Layer]
    C --> D[Gold Layer]
    D --> E[Analytics Layer]
    E --> F[Power BI Dashboards]
```

1. **Bronze Layer** - Raw export data is ingested
2. **Silver Layer** - Data is cleaned and standardized
3. **Gold Layer** - Aggregated KPIs are generated
4. **Analytics Layer** - Forecasting and emerging market detection
5. **Visualization** - Final datasets consumed by Power BI dashboards

---

## 4. Technology Stack

### Core Technologies

| Category | Technologies |
|----------|-------------|
| **Data Processing & Analytics** | Python, Pandas, NumPy, PySpark, Databricks |
| **Workflow Orchestration** | Apache Airflow |
| **Data Storage** | CSV, Delta Lake (future) |
| **Visualization** | Power BI |
| **Version Control** | Git & GitHub |
| **Development Environment** | Jupyter / Databricks Notebooks |

---

## 5. Data Architecture (Bronze–Silver–Gold)

### Bronze Layer – Raw Ingestion

- Ingests raw export CSV files
- Performs schema validation
- Handles ingestion errors and logging
- Stores raw data in its original structure

### Silver Layer – Cleaning & Standardization

- Handles missing and inconsistent values
- Standardizes country codes and product categories
- Ensures correct data types
- Produces analytics-ready cleaned datasets

### Gold Layer – Aggregations & KPIs

- Aggregates exports by country, region, year, and product
- Computes key trade metrics and KPIs
- Produces final datasets for reporting and analytics

### Analytics Layer

- **Forecasting** of export trends
- **Identification** of emerging export markets
- **Detection** of declining sectors

---

## 6. Databricks Notebooks

### Pipeline Notebooks

| # | Notebook | Purpose |
|---|----------|---------|
| 1 | `01_capstone_bronze.ipynb` | Raw data ingestion (Bronze layer) |
| 2 | `02_capstone_silver.ipynb` | Data cleaning and standardization |
| 3 | `03_capstone_gold.ipynb` | Aggregations and KPI generation |
| 4 | `04_capstone_forecasting.ipynb` | Export trend forecasting |
| 5 | `05_capstone_emerging_markets.ipynb` | Emerging market identification |

---

## 7. Airflow Workflow Orchestration

### Overview

Apache Airflow is used to orchestrate the ETL pipeline and Databricks notebooks.

### DAG Configuration

- **DAG Name:** `global_trade_bronze_silver_gold_pipeline`
- **Schedule:** Daily
- **Purpose:** Orchestrate execution of Databricks notebooks

### Task Flow

```mermaid
graph LR
    A[capstone_bronze] --> B[capstone_silver]
    B --> C[capstone_gold]
    C --> D[capstone_forecasting]
    D --> E[capstone_emerging_markets]
```

**Pipeline Flow:**
```
capstone_bronze → capstone_silver → capstone_gold → [capstone_forecasting, capstone_emerging_markets]
```

> **Note:** Each Airflow task represents a Databricks job execution. Placeholders are used for job IDs in academic/testing environments.

---

## 8. Data Validation & Quality Checks

### Quality Assurance

- **Row count reconciliation** across layers
- **Null and missing value** handling verification
- **Aggregation accuracy** checks
- **Year-over-year metric** validation
- **Power BI dashboard** data verification

> All data quality checks are automated and run as part of each layer's processing pipeline.

---

## 9. Visualization & Reporting (Power BI)

### Dashboard Overview

Power BI dashboards are built on Gold and analytics datasets.

### Dashboard Components:

- **Global export performance** overview
- **Country-wise export** comparison
- **Product-wise export** trends
- **Regional trade** performance
- **Key trade KPIs** for policymakers

> These dashboards enable interactive analysis and decision support for trade policy makers and business analysts.

---

## 10. Key Business Insights

### Analytics Outcomes

- **Identification** of top exporting countries and products
- **Detection** of high-growth regions
- **Recognition** of declining trade sectors
- **Emerging export market** identification
- **Forecast-based** trade trend insights

> These insights support strategic decision-making for trade policy, market entry, and economic development planning.

---

## 11. Testing & Validation

### Testing Strategy

- **ETL pipeline** correctness validation
- **Airflow DAG** execution verification
- **Spark transformation** validation
- **Dashboard accuracy** checks
- **Data quality** assertions at each layer

---

## 12. Limitations & Future Enhancements

### Current Limitations

- **Batch-based processing** only
- **Databricks jobs** triggered conceptually via Airflow (placeholders used)
- **Local storage** instead of cloud infrastructure

### Future Scope

- **Real-time data ingestion** using Apache Kafka
- **Direct Airflow–Databricks** job integration
- **Cloud data warehouse** integration (Snowflake/BigQuery)
- **Advanced ML-based** trade forecasting models
- **API endpoints** for real-time data access
- **Alert system** for anomaly detection

---

## 13. Repository Structure

### Project Layout

```
capstone/
├── airflow_project/
│   ├── airflow/
│   ├── airflow_env/        # Python virtual environment
│   ├── dags/
│   ├── logs/
│   ├── airflow.cfg
│   ├── airflow.db
│   └── webserver_config.py
├── data/
│   ├── processed/
│   └── raw/
├── databricks notebooks/
│   ├── capstone_bronze.ipynb
│   ├── capstone_emerging_markets.ipynb
│   ├── capstone_forecasting.ipynb
│   ├── capstone_gold.ipynb
│   └── capstone_silver.ipynb
├── powerBI/
│   └── capstonePowerBIFile.pbix
└── README.md
```

---

## 14. Getting Started

### Prerequisites

- Python 3.10+
- Apache Airflow
- Databricks workspace (or local Spark for testing)
- Power BI (for dashboards)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repo_url>
cd capstone
```

#### 2. Set Up Python Environment
```bash
python -m venv airflow_env

# Linux/Mac
source airflow_env/bin/activate

# Windows
.\airflow_env\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Airflow
```bash
# Linux/Mac
export AIRFLOW_HOME=$(pwd)/airflow_project

# Windows PowerShell
$env:AIRFLOW_HOME="$(Get-Location)\airflow_project"
```

#### 5. Initialize Airflow Database
```bash
airflow db init
```

#### 6. Start Airflow Services
```bash
# Terminal 1: Start webserver
airflow webserver --port 8080

# Terminal 2: Start scheduler
airflow scheduler
```

#### 7. Access Airflow UI
Open your browser and navigate to: `http://localhost:8080`

### Quick Start Guide

1. Place your raw export CSV files in `data/raw/`
2. Access Airflow UI and enable the DAG
3. Trigger the pipeline manually or wait for scheduled run
4. Monitor execution in Airflow UI
5. Access processed data in `data/processed/`
6. Open Power BI dashboard from `powerBI/` folder

---

## 15. Acknowledgements

### Credits

- Datasets and insights inspired by publicly available trade statistics
- Power BI and Databricks documentation
- Apache Airflow tutorials and academic examples
- Best practices from data engineering community

---

## Contact & Support

For questions or issues:
- Open an issue in this repository
- Refer to documentation in individual notebooks
- Check Airflow logs in `airflow_project/logs/`

---

## License

This project is created for educational and demonstration purposes.

---

**Built for Data Engineering Excellence**