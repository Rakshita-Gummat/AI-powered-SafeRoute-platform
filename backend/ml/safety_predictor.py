import os
import joblib
import pandas as pd

# Load trained model
BASE_DIR = os.path.dirname(__file__)
FINAL_MODEL_PATH = os.path.join(BASE_DIR, "final_safety_model.pkl")

_bundle = joblib.load(FINAL_MODEL_PATH)

_model = _bundle["model"]
FEATURE_COLS = _bundle["features"]
METRICS = _bundle.get("metrics", {})


def build_feature_vector(street_row: dict) -> pd.DataFrame:
    """
    Convert MongoDB street document into a dataframe
    using SAME feature order as training.
    """

    values = {}

    for col in FEATURE_COLS:
        val = street_row.get(col, 0)

        try:
            val = float(val)
        except (TypeError, ValueError):
            val = 0.0

        values[col] = val

    # Return dataframe with proper feature names
    return pd.DataFrame([values], columns=FEATURE_COLS)


def predict_safety_score(street_row: dict) -> float:
    """
    Predict safety score (1–5)
    """

    x = build_feature_vector(street_row)

    score = float(_model.predict(x)[0])

    # Clamp score
    score = max(1.0, min(5.0, score))

    return score


def categorize(score: float) -> str:
    """
    Convert numeric score into category
    """

    if score < 2.5:
        return "unsafe"

    elif score < 3.5:
        return "moderate"

    return "very_safe"