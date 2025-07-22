# src/airflow/scripts/retrain_runner.py

import os
import sys

# Add root path to sys.path for absolute imports to work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.ml.training.train import train_all_models

def run_retrain():
    """
    Retrains the lead scoring model using the full reference dataset,
    saves artifacts, and registers/promotes the pipeline in MLflow.

    Returns:
        bool: True when retraining completes successfully.
    """
    # 1) Ensure MLflow tracking URI is configured
    mlflow_uri = os.getenv("MLFLOW_TRACKING_URI")
    if not mlflow_uri:
        raise EnvironmentError("MLFLOW_TRACKING_URI environment variable is not set")

    # Ensure it's set in environment as well
    os.environ["MLFLOW_TRACKING_URI"] = mlflow_uri

    # 2) Trigger full training of all models with proper table and target column
    train_all_models()

    # 3) Indicate successful execution (used by Airflow BranchPythonOperator)
    return True
