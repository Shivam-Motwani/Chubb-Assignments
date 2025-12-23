# Enterprise Data Engineering Project

## Technologies

![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF6C37?logo=databricks)
![Apache Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-00ADD8)
![Power BI](https://img.shields.io/badge/Power-BI-F2C811?logo=powerbi)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture & Design](#architecture--design)
- [Data Model Documentation](#data-model-documentation)
- [Incremental Processing Logic](#incremental-processing-logic)
- [Data Quality & Calibration](#data-quality--calibration)
- [Logging & Monitoring](#logging--monitoring)
- [Security & Enterprise Considerations](#security--enterprise-considerations)
- [Power BI Dashboards](#power-bi-dashboards)
- [Validation Summary](#validation-summary)
- [Submission Package](#submission-package)

---

## Project Overview

### Business Problem Statement

The company aims to build a modern analytics platform for sales data to:

- Track daily and monthly sales
- Analyze product performance
- Monitor revenue by region
- Provide interactive dashboards for business decisions

### Business Questions Addressed

- What is the total revenue daily, monthly, and by region?
- Which products perform best in sales and revenue?
- How does regional performance compare across stores?

### Assumptions

- **Data Volume**: ~1000 rows for simulation; can scale to millions
- **Data Frequency**: Daily transactional updates
- **Data Quality**: May include duplicates, nulls, and invalid entries

### Success Criteria

- Bronze, Silver, and Gold layers ingested correctly
- Data cleaned and calibrated in Silver
- Gold tables accurate and optimized for analytics
- Power BI dashboards reflect correct metrics and trends

---

## Architecture & Design

### High-Level Architecture

```
Source Systems → Bronze Layer → Silver Layer → Gold Layer → Power BI
```

### Tool Roles

| Tool | Purpose |
|------|---------|
| **Databricks** | Orchestrates Spark jobs and manages notebooks |
| **Apache Spark** | Performs distributed data processing |
| **Delta Lake** | Handles ACID transactions, schema enforcement, and time travel |
| **Power BI** | Visualizes Gold layer data for business insights |

### Data Flow

- **Bronze**: Raw ingestion with metadata (`ingestion_timestamp`, `source_system`)
- **Silver**: Deduplication, cleansing, calibration, and quarantine handling
- **Gold**: Business aggregations for daily, monthly, and product-level metrics

### Naming Conventions

```
Bronze: workspace.default.bronze_*
Silver: workspace.default.silver_*
Gold:   workspace.default.gold_*
```

### Partitioning Strategy

- **Bronze**: `ingestion_date`
- **Silver**: `transaction_date`
- **Gold**: `sales_date` or `month`

---

## Data Model Documentation

### Bronze Layer

**Tables**: `bronze_sales_transactions`, `bronze_product_master`, `bronze_store_region`

- **Columns**: All raw source columns + metadata
- **Purpose**: Preserve raw source data for audit and recovery

### Silver Layer

**Tables**: `silver_sales_transactions`, `silver_sales_quarantine`

**Transformations**:
- Deduplicate records based on `transaction_id`
- Handle null values
- Recalculate `total_amount = quantity × unit_price – discount`
- Quarantine invalid records

**Purpose**: Clean and validated dataset for analytics

### Gold Layer

**Tables**: `gold_daily_sales`, `gold_monthly_revenue`, `gold_product_metrics`

**Transformations**: Aggregations for daily sales, monthly revenue, and product performance

**Purpose**: Analytics-ready dataset for reporting and dashboards

### Relationships in Power BI

- Tables linked via `product_id`, `store_id`, and `date`
- Enables filtering and drill-down across visuals

---

## Incremental Processing Logic

- **Bronze Layer**: Append-only ingestion, partitioned by `ingestion_date`
- **Silver Layer**: Processes only new or changed records using Delta MERGE; quarantines invalid data
- **Gold Layer**: Aggregates only the updated Silver records to compute daily/monthly metrics

---

## Data Quality & Calibration

### Validation Rule

```
total_amount = quantity × unit_price – discount
```

### Corrections Applied

- Recalculate incorrect totals
- Normalize currency values
- Enforce numeric precision to two decimals

### Data Quality Checks

- `quantity > 0`
- `unit_price > 0`
- Valid `store_id` and `product_id`

---

## Logging & Monitoring

### Table: `pipeline_logs`

**Columns**: 
- `pipeline_layer`
- `records_processed`
- `records_rejected`
- `status`
- `start_ts`
- `end_ts`
- `remarks`

### Usage

- Logs start, end, and failures for each layer
- Tracks valid and rejected records
- Supports reruns and prevents duplication

---

## Security & Enterprise Considerations

### Access Control

| Layer | Access |
|-------|--------|
| **Bronze** | Data engineers only |
| **Silver** | Data engineers + analysts |
| **Gold** | Analysts + business users |

### Environment Separation

`Dev` → `Test` → `Prod`

### Data Lineage

Documented flow: `Source → Bronze → Silver → Gold`

### Data Protection

- Delta versioning
- Optional masking of sensitive fields

---

## Power BI Dashboards

### Dashboards Developed

1. **Executive Sales Dashboard**
   - Total revenue
   - Revenue trends
   - Regional breakdown

2. **Product Performance Dashboard**
   - Top products
   - Category-wise revenue
   - Monthly trends

### Key Visuals

- Line charts for sales trends
- Bar charts for top products and categories
- Regional map for sales distribution
- Slicers for filtering by date, region, and product category

### Relationships

- Gold tables connected via `product_id`, `store_id`, and `date`
- Ensures correct aggregation and drill-down

---

## Validation Summary

- Bronze, Silver, Gold layers validated for record counts
- Silver data calibrated correctly; invalid records quarantined
- Gold aggregations match Silver totals
- Logging confirmed for all pipeline layers
- Power BI visuals match expected metrics and trends

---

## Submission Package

- **Databricks Notebooks**: Bronze, Silver, Gold, Logging, Validation
- **Power BI Report**: `.pbix` file
- **Documentation**: This README file

---

**Last Updated**: December 2025