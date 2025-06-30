"""
Configuración del proyecto de predicción de diabetes.
Este archivo centraliza todos los parámetros y configuraciones.
"""

import os
from pathlib import Path

# === PATHS DEL PROYECTO ===
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
MLRUNS_DIR = PROJECT_ROOT / "mlruns"

# Archivos específicos
DIABETES_DATA_PATH = DATA_DIR / "diabetes.csv"

# === CONFIGURACIÓN DE MLFLOW ===
MLFLOW_EXPERIMENT_NAME = "Diabetes Prediction"
MLFLOW_TRACKING_URI = None  # None = local filesystem

# === CONFIGURACIÓN DEL MODELO ===
# Seed para reproducibilidad
RANDOM_STATE = 42

# División de datos
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

# Columnas que pueden tener 0s como valores faltantes
ZERO_TO_NAN_COLUMNS = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Variables objetivo y features
TARGET_COLUMN = 'Outcome'
FEATURE_COLUMNS = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
]

# === HIPERPARÁMETROS POR DEFECTO ===
DEFAULT_RF_PARAMS = {
    'n_estimators': 100,
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'random_state': RANDOM_STATE
}

# === CONFIGURACIONES DE EXPERIMENTACIÓN ===
# Para búsqueda de hiperparámetros
HYPERPARAMETER_GRID = {
    'n_estimators': [50, 100, 150, 200],
    'max_depth': [3, 5, 8, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4, 8]
}

# Métrica principal para selección de modelo
PRIMARY_METRIC = 'f1_score'

# === CONFIGURACIÓN DE LOGGING ===
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
