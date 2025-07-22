# Structure of the Project 
```text
.                                                       # Root project directory
├── Final_Outputs                                       # Screenshots of each step for documentation/evidence
│   ├── AFTER DATA UPLOADED BY USER BACKEND( Step 12)   # Backend validation after user uploads data
│   ├── Airflow (Step 13)                               # Airflow UI screenshots after DAG run
│   ├── CRAWLER(Step 5)                                 # Screenshots of the web crawler setup
│   ├── Dirft logs (Step 14)                            # Screenshots of drift report logs from Airflow
│   ├── EC2 (MLFLOW) [STEP 8]                           # EC2 instance setup for MLflow
│   ├── Final Flask Code (Step 13)                      # Flask backend UI and API screenshots
│   ├── Glue connections (Step 6)                       # AWS Glue crawler and connection setup
│   ├── IAM                                             # IAM roles and permissions
│   ├── Inital S3 with Lead  Data(Step 1)               # Initial data upload to S3
│   ├── MLflow (Step 10)                                # Screenshots of MLflow model tracking
│   ├── REDSHIFT (Step 4)                               # Amazon Redshift setup and tables
│   ├── S3 - REDSHIFT (Step 7)                          # S3 to Redshift connection proof
│   ├── S3 Buckets Final State with all files(Step 15)  # Final structure of S3 with all files
│   ├── Security Groups (Step 2)                        # Security Group configuration screenshots
│   ├── Training (Step 9)                               # Model training pipeline run on EC2
│   ├── User uploads Data(Step 11)                      # Frontend where user uploads CSV
│   └── Vpc Endpoints  (Step 3)                         # VPC endpoints setup for private access
├── README.md                                           # Project instructions and documentation
├── data                                                # Local data used for EDA and modeling
│   ├── eda_report.html                                 # Auto-generated EDA report
│   ├── lead_scoring.csv                                # Raw training dataset
│   └── test_lead_scoring.csv                           # Test dataset for validation
├── lead_data_schema.txt                                # Schema of the incoming data file
├── models                                              # Pickled models and preprocessing pipelines
│   ├── full_pipeline.pkl                               # Pipeline with preprocessing steps
│   ├── full_pipeline_with_model.pkl                    # Full pipeline including model
│   └── preprocessor.pkl                                # Only preprocessing object
├── reports
│   └── drift                                           # Data drift reports (HTML + JSON)
│       ├── drift_lead_data_vs_uploaded_*.html/json     # Drift between base data and uploaded
│       └── drift_train_vs_test_*.html/json             # Drift between train and test data
├── requirements.txt                                    # Python dependencies
├── scripts                                             # Manual scripts to run specific jobs
│   ├── load_data_to_postgres.py                        # Script to upload data to PostgreSQL
│   └── run_drift.py                                    # Script to trigger drift calculation
├── src                                                 # Main source code directory
│   ├── airflow                                         # Airflow DAGs and metadata setup
│   │   ├── airflow.cfg                                 # Configuration file for Airflow
│   │   ├── airflow.db                                  # Metadata DB (SQLite)
│   │   ├── dags                                        # All DAG files
│   │   │   └── drift_retrain_dag.py                    # Main DAG for drift detection + retraining
│   │   ├── logs                                        # Airflow log output
│   │   ├── scripts                                     # Airflow DAG-triggered scripts
│   │   │   ├── check_drift_runner.py                   # Checks data drift
│   │   │   ├── retrain_runner.py                       # Triggers retraining process
│   │   │   └── trigger_upload_monitor.py               # Monitors S3 uploads
│   │   ├── utils
│   │   │   └── airflow_loader.py                       # Loads DAG configurations and variables
│   │   └── webserver_config.py                         # Config for Airflow webserver
│   ├── app                                             # Flask app backend
│   │   ├── main.py                                     # Main Flask entry point
│   │   ├── routes.py                                   # API endpoints for user interaction
│   │   ├── templates/index.html                        # Frontend upload interface
│   │   └── utils
│   │       ├── prediction.py                           # Code to make predictions
│   │       └── upload.py                               # Validates and uploads user CSV
│   ├── db                                              # Database connection helpers
│   │   └── db_utils.py                                 # Helper to connect/query PostgreSQL
│   ├── drift                                           # Drift detection logic
│   │   ├── check_drift.py                              # Drift check between datasets
│   │   └── test_dirft.py                               # Unit tests for drift module
│   ├── eda                                             # Exploratory Data Analysis tools
│   │   └── profiler.py                                 # Code for generating EDA reports
│   ├── logs                                            # Custom logs
│   └── ml                                              # Machine learning modules
│       ├── data_loader/data_loader.py                 # Loads raw or preprocessed data
│       ├── evaluation/                                 # Model evaluation and comparison
│       │   └── metrics.py                              # Accuracy, precision, recall etc.
│       ├── model_objects/                              # Saved models for comparison
│       ├── pipeline/                                   # Pipeline construction
│       │   ├── custom_transformers.py                  # Custom transformers used in pipeline
│       │   ├── feature_engineering.py                  # Feature engineering logic
│       │   ├── feature_selection.py                    # Feature selection strategies
│       │   ├── feature_selector.py                     # Custom transformer to select features
│       │   ├── pipeline_runner.py                      # Pipeline runner script
│       │   ├── preprocessing.py                        # Preprocessing logic
│       │   └── schema_validator.py                     # Validates incoming dataframe schema
│       ├── registry/model_registry.py                  # Registers and loads models from disk
│       └── training/                                   # Training logic
│           ├── mlflow_logger.py                        # Logs metrics and models to MLflow
│           ├── train.py                                # Runs the full model training pipeline
│           └── train_utils.py                          # Utilities for training
├── structure.txt                                       # Alternate structure file (likely unused)
├── struture.txt                                        # Typo'd duplicate, likely can be removed
└── uploads                                             # Uploaded CSVs from users
    ├── Lead_Scoring.csv                                # Uploaded training data
    ├── predicted_data.csv                              # Output file with model predictions
    ├── sample_data.csv                                 # Sample format for uploads
    └── test_Lead_Scoring.csv                           # Uploaded test data
```


# Sample Env
```text ==========================
 🛠️ DATABASE CONFIGURATION
 ==========================
DB_USER=your_db_username_here
DB_PASSWORD=your_db_password_here
DB_HOST=your_db_host_here           # e.g., localhost or Redshift hostname
DB_PORT=your_db_port_here           # e.g., 5432
DB_NAME=your_database_name_here

 ====================
 📊 TABLE NAMES SETUP
 ====================
DB_TABLE=your_main_table_name               # e.g., lead_data
DB_TEST_TABLE_UPLOADED=your_test_table      # e.g., test_lead_data
DB_TABLE_PREPROCESSED=your_preprocessed_table   # e.g., preprocessed_train_data
DB_NEW_TABLE_PREPROECESSED=user_uploaded_preprocessed  # table for newly uploaded preprocessed data

 ================================
 🚀 MLFLOW TRACKING CONFIGURATION
 ================================
MLFLOW_TRACKING_URI=http://localhost:5000   # or your remote MLflow URI
```

# 🛫 Example Setup: Airflow with PostgreSQL for Lead Scoring System

> ⚠️ **NOTE:** All names used here (e.g., database names, project folder paths, user details) are just examples.  
> Please **replace them with your own values** according to your system or project setup.

---

## 🧰 Installation Prerequisites
```text
- OS: WSL (Ubuntu) or native Ubuntu system
- Environment: Conda environment (example name: `lead_pipeline_env`)
- Python: Version 3.10 installed
- Project Directory: (example) `~/Projects/lead_pipeline_project/src/airflow/`
```

---

## 📦 Step 1 – Install PostgreSQL
```text
sudo apt update
sudo apt install postgresql postgresql-contrib
```

---

## 🛠️ Step 2 – Configure PostgreSQL (Example Setup)
```text
# Creates a new PostgreSQL database named 'lead_db_example'
sudo -u postgres psql -c "CREATE DATABASE lead_db_example;"

# (Optional) Enter PostgreSQL CLI for advanced operations
sudo -u postgres psql
```

---

## 🧪 Step 3 – Validate the DB in CLI (Optional)
```text
\l                             # List all available databases
\c lead_db_example            # Connect to the example database
select * from uploaded_leads limit 10;  # Example table query (if table exists)
```

---

## 🐍 Step 4 – Install Airflow in Conda
```text
conda activate lead_pipeline_env  # Replace with your env name

pip install "apache-airflow==2.10.0" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.0/constraints-3.8.txt"
```

---

## 🏗️ Step 5 – Configure Shell Environment
```text
# Open shell config based on your shell
nano ~/.bashrc        # For bash users
nano ~/.zshrc         # For zsh users

# Add these lines (with your paths/envs):
export AIRFLOW_HOME=~/Projects/lead_pipeline_project/src/airflow
conda activate lead_pipeline_env

# Save and reload config
Ctrl + O → Enter → Ctrl + X
source ~/.bashrc
```

---

## 🔍 Step 6 – Verify Configuration
```text
echo $AIRFLOW_HOME     # Should output your AIRFLOW project directory
which airflow          # Should show path inside your conda env

# (Optional) Remove default Airflow directory
rm -rf ~/airflow
```

---

## 🗃️ Step 7 – Initialize Airflow DB
```text
airflow db init
```

---

## 👤 Step 8 – Create Airflow Admin User
```text
# Replace user details with your own
airflow users create \
    --username admin \
    --firstname John \
    --lastname Doe \
    --role Admin \
    --email john.doe@example.com
```

---

## 🚀 Step 9 – Run Airflow Services
```text
# Terminal 1
airflow webserver --port 8080

# Terminal 2
airflow scheduler
```

---

## 🌐 Step 10 – Open Airflow UI
```text
Go to: http://localhost:8080

Login using:
  Username: admin
  Password: (as set during user creation)
```

---

## 📁 Example Project Structure
```text
src/airflow/
├── airflow.cfg         # Configuration file
├── airflow.db          # Metadata DB (SQLite for dev only)
├── dags/               # DAGs go here
└── logs/               # Execution logs by date and task
```

# How to run the project
if no data is available 
```text 
python scripts/load_data_to_postgres
```
Training the model
```text
python src/ml/training/train.py
```

Run the flask app
```text 
Run the mlflow first -- mlflow ui
Run the python script -- python src/app/main.py
```

Run the airflow
```text 
airflow webserver
airflow scheduler
```
---

## ⚙️ Behavior on Startup
```text
- The AIRFLOW_HOME variable is auto-loaded via shell
- Your Conda environment (example: `lead_pipeline_env`) activates automatically
- All Airflow files are kept inside `src/airflow/` for clean organization
```

---

✅ **Use this setup for example workflows like:**
- Lead scoring
- Data ingestion
- Model retraining
- Drift detection scheduling


# This is a new  repo because of the old repo got misconifgured
old repo link - https://github.com/VenkatSaiMinfy/Final_Capstone_Local_Development

# For Production Level Code Access this repo
```text
https://github.com/VenkatSaiMinfy/Final_Capstone_Production
```