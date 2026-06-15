"""
config.py - Configuracion centralizada del proyecto TFM
Todas las rutas, seeds y parametros en un solo lugar.
"""
from pathlib import Path

# === RUTAS ===
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_NLP = PROJECT_ROOT / "data" / "nlp"
REPORTS_FIGURES = PROJECT_ROOT / "reports" / "figures"
REPORTS_SHAP = PROJECT_ROOT / "reports" / "shap"
REPORTS_TABLES = PROJECT_ROOT / "reports" / "tables"
OUTPUTS = PROJECT_ROOT / "outputs"

# === ARCHIVOS DE DATOS ===
IBM_HR_FILE = DATA_RAW / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
EXTENDED_HR_FILE = DATA_RAW / "general_data.csv"
GLASSDOOR_FILE = DATA_RAW / "glassdoor_reviews.csv"

# === REPRODUCIBILIDAD ===
RANDOM_SEED = 42
TEST_SIZE = 0.20

# === TARGET ===
TARGET_COL = "Attrition"
TARGET_MAP = {"Yes": 1, "No": 0}

# === VARIABLES A ELIMINAR ===
DROP_COLS_IBM = ["EmployeeCount", "Over18", "StandardHours", "EmployeeNumber"]

# === NLP ===
SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
ZERO_SHOT_MODEL = "facebook/bart-large-mnli"
NLP_TOPICS = ["leadership", "burnout", "compensation", "culture", "communication", "career_growth"]
MAX_TOKENS_NLP = 512

# === MODELOS ML ===
MODELS_CONFIG = {
    "LogisticRegression": {"class_weight": "balanced", "max_iter": 1000, "random_state": RANDOM_SEED},
    "RandomForest": {"n_estimators": 100, "class_weight": "balanced", "random_state": RANDOM_SEED},
    "XGBoost": {"n_estimators": 200, "max_depth": 4, "learning_rate": 0.1, "random_state": RANDOM_SEED},
    "SVM": {"kernel": "rbf", "class_weight": "balanced", "probability": True, "random_state": RANDOM_SEED},
    "MLP": {"hidden_layer_sizes": (64, 32), "max_iter": 500, "random_state": RANDOM_SEED},
}

# === METRICAS ===
SCORING_METRIC = "roc_auc"
CV_FOLDS = 5

# === GRAFICAS ===
FIG_DPI = 150
FIG_FORMAT = "png"

# === COSTES EMPRESARIALES ===
REPLACEMENT_COST_PCT = 0.75
HR_ACTION_RATE = 0.60
