import os
import random

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from data import MODEL_CROP_PROFILES


MODEL_PATH = os.path.join("model", "crop_model.pkl")
ENCODER_PATH = os.path.join("model", "label_encoder.pkl")


def random_between(value_range):
    low, high = value_range
    return random.uniform(low, high)


def build_training_data(samples_per_crop=45):
    random.seed(42)
    x_data = []
    y_data = []

    for crop_name, profile in MODEL_CROP_PROFILES.items():
        for _ in range(samples_per_crop):
            row = [
                random_between(profile["n"]),
                random_between(profile["p"]),
                random_between(profile["k"]),
                random_between(profile["temp"]),
                random_between(profile["humidity"]),
                random_between(profile["ph"]),
                random_between(profile["rainfall"]),
            ]
            x_data.append(row)
            y_data.append(crop_name)

    return x_data, y_data


def train_and_save_model():
    os.makedirs("model", exist_ok=True)
    x_data, y_data = build_training_data()

    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(y_data)

    model = RandomForestClassifier(n_estimators=60, random_state=42)
    model.fit(x_data, encoded_labels)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_encoder, ENCODER_PATH)

    print("Model trained successfully.")
    print(f"Saved: {MODEL_PATH}")
    print(f"Saved: {ENCODER_PATH}")


if __name__ == "__main__":
    train_and_save_model()
