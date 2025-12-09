# Apache Airflow ETL Pipeline - Assignment 4

## Overview
This project implements a daily ETL pipeline using Apache Airflow to process e-commerce data for ShopVerse. The pipeline ingests customer, product, and order data from multiple source systems, applies transformations, and loads the results into a PostgreSQL data warehouse following a star schema design.

## Project Structure
```
Assignment-4 Airflow/
├── Dags/
│   └── shopverse_daily_pipeline.py    Main DAG implementation
├── sql/
│   ├── creating_staging_tables.sql    Staging table definitions
│   └── creating_warehouse_tables.sql  Dimension and fact table definitions
└── screenshots/
    └── pipeline-graph.jpg             DAG visualization
```

## Pipeline Architecture

### Data Flow
1. File Sensors wait for three daily input files
   - customers_{YYYYMMDD}.csv
   - products_{YYYYMMDD}.csv
   - orders_{YYYYMMDD}.json

2. Staging Layer
   - Raw data loaded into staging tables
   - Tables truncated before each load to ensure clean state

3. Warehouse Layer
   - Dimension tables (customers, products) built with deduplication
   - Fact table (orders) created with transformations

4. Data Quality Checks
   - Validate dimension tables are populated
   - Ensure referential integrity in fact table
   - Verify row counts match between staging and warehouse

5. Anomaly Detection
   - Branch based on order volume
   - Generate reports for low-volume days

### Key Transformations
- Timestamp normalization to UTC
- Currency standardization with mismatch flagging
- Duplicate removal using window functions
- Data validation to filter invalid records

## Database Schema

### Staging Tables
- stg_customers: Raw customer data
- stg_products: Raw product catalog
- stg_orders: Raw order transactions

### Warehouse Tables
- dim_customers: Customer dimension with business key
- dim_products: Product dimension with current state
- fact_orders: Order fact table with foreign keys to dimensions

## Configuration Requirements

### Airflow Variables
Set these in Airflow UI under Admin > Variables:
- shopverse_data_base_path: Base directory for data files
- shopverse_min_order_threshold: Minimum daily orders before alerting
- notification_email: Email address for alerts

### Airflow Connections
Create connection in Airflow UI under Admin > Connections:
- Connection ID: postgres_dwh
- Connection Type: Postgres
- Host: PostgreSQL server hostname
- Database: dwh_shopverse
- Username: heavens (mine, use yours)
- Password: "use yours"
- Port: 5432

### File System Connection
- Connection ID: fs_default
- Connection Type: File (path)
- Extra: {"path": "/path/to/data"}

## Installation Steps

1. Set up PostgreSQL database
```sql
CREATE DATABASE dwh_shopverse;
```

2. Create tables using provided SQL scripts
```bash
psql -d dwh_shopverse -f sql/creating_staging_tables.sql
psql -d dwh_shopverse -f sql/creating_warehouse_tables.sql
```

3. Configure Airflow variables and connections as described above

4. Place DAG file in Airflow dags folder
```bash
cp Dags/shopverse_daily_pipeline.py $AIRFLOW_HOME/dags/
```

5. Ensure data files follow naming convention and are placed in configured directory

## Running the Pipeline

### Manual Execution
Access Airflow web UI and trigger the DAG manually for testing.

### Backfilling
To process historical dates:
```bash
airflow dags backfill shopverse_daily_pipeline \
  --start-date 2025-01-01 \
  --end-date 2025-01-05
```

### Scheduled Execution
Pipeline runs automatically at 1:00 AM daily for previous day's data.

## Data Quality Checks

The pipeline implements three critical validations:

1. Dimension Population
   - Ensures customer dimension is not empty
   - Fails pipeline if no customers loaded

2. Referential Integrity
   - Checks for NULL foreign keys in fact table
   - Validates all orders reference valid customers and products

3. Completeness
   - Compares fact table count with staging valid records
   - Ensures no data loss during transformation

## Monitoring and Alerts

### Success Indicators
- All tasks show green status in DAG graph
- Email notification sent on successful completion
- Data quality checks pass

### Failure Handling
- Pipeline stops at first failure
- Email alert sent with error details
- Failed task can be cleared and rerun

### Low Volume Detection
- Orders below threshold trigger anomaly branch
- Report generated in anomalies directory
- Warning logged but pipeline continues

## Technical Implementation

### Airflow Features Used
- TaskFlow API for Python tasks with XCom
- TaskGroups for logical organization
- FileSensors for file arrival detection
- SQLExecuteQueryOperator for SQL transformations
- BranchPythonOperator for conditional logic
- PostgresHook for database operations

### Design Decisions
- Staging tables truncated to ensure idempotency
- Fact table deletes by date to support reprocessing
- Upsert pattern in dimensions for slowly changing data
- Window functions for deduplication
- Parameterized queries to prevent SQL injection

## Troubleshooting

### Files Not Detected
- Verify file naming matches pattern with date suffix
- Check file permissions allow Airflow read access
- Ensure fs_default connection path is correct

### Database Connection Failures
- Test connection from Airflow UI
- Verify PostgreSQL is running and accessible
- Check network firewall rules

### Data Quality Failures
- Review staging table contents for data issues
- Check source file quality
- Examine transformation SQL logic

### Performance Issues
- Consider indexing frequently queried columns
- Adjust poke_interval on sensors
- Review query execution plans

## Maintenance

### Regular Tasks
- Monitor anomaly reports for business trends
- Review failed task logs
- Archive processed files
- Vacuum PostgreSQL tables periodically

### Updates
- Test DAG changes in development environment
- Use version control for DAG files
- Document configuration changes

## Contact
For questions or issues, contact me.
