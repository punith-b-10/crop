import os

import joblib
from flask import Flask, jsonify, render_template, request

from data import CROP_INFO, MODEL_CROP_PROFILES, get_crop_info_list
from train_model import ENCODER_PATH, MODEL_PATH, train_and_save_model


app = Flask(__name__)


def load_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
        train_and_save_model()

    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    return model, label_encoder


model, label_encoder = load_model()


def get_float(field_name):
    value = request.json.get(field_name)
    if value is None or value == "":
        raise ValueError(f"{field_name} is required")
    return float(value)


def range_score(value, value_range):
    low, high = value_range
    middle = (low + high) / 2
    half_width = (high - low) / 2

    if half_width == 0:
        return 1

    distance = abs(value - middle)
    return max(0, 1 - (distance / (half_width * 1.6)))


def estimate_yield(crop_name, inputs):
    profile = MODEL_CROP_PROFILES[crop_name]
    scores = [
        range_score(inputs["nitrogen"], profile["n"]),
        range_score(inputs["phosphorus"], profile["p"]),
        range_score(inputs["potassium"], profile["k"]),
        range_score(inputs["temperature"], profile["temp"]),
        range_score(inputs["humidity"], profile["humidity"]),
        range_score(inputs["ph"], profile["ph"]),
        range_score(inputs["rainfall"], profile["rainfall"]),
    ]
    suitability = sum(scores) / len(scores)
    estimated_yield = profile["yield"] * (0.65 + suitability * 0.45)
    return round(estimated_yield, 2), round(suitability * 100, 1)


@app.route("/")
def home():
    return render_template("index.html", crops=get_crop_info_list())


@app.route("/predict", methods=["POST"])
def predict():
    try:
        inputs = {
            "nitrogen": get_float("nitrogen"),
            "phosphorus": get_float("phosphorus"),
            "potassium": get_float("potassium"),
            "temperature": get_float("temperature"),
            "humidity": get_float("humidity"),
            "ph": get_float("ph"),
            "rainfall": get_float("rainfall"),
        }
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    feature_row = [[
        inputs["nitrogen"],
        inputs["phosphorus"],
        inputs["potassium"],
        inputs["temperature"],
        inputs["humidity"],
        inputs["ph"],
        inputs["rainfall"],
    ]]

    probabilities = model.predict_proba(feature_row)[0]
    top_indexes = probabilities.argsort()[-3:][::-1]
    crop_names = label_encoder.inverse_transform(top_indexes)

    recommendations = []
    for index, crop_name in zip(top_indexes, crop_names):
        estimated_yield, suitability = estimate_yield(crop_name, inputs)
        crop_info = CROP_INFO.get(crop_name, {})
        recommendations.append({
            "crop": crop_name,
            "confidence": round(float(probabilities[index]) * 100, 1),
            "estimated_yield": estimated_yield,
            "suitability": suitability,
            "price": crop_info.get("price"),
            "demand": crop_info.get("demand"),
            "season": crop_info.get("season"),
            "tips": crop_info.get("tips"),
            "image": crop_info.get("image"),
        })

    return jsonify({"recommendations": recommendations})


@app.route("/market/<crop_name>")
def market(crop_name):
    crop = CROP_INFO.get(crop_name)
    if crop is None:
        return jsonify({"error": "Crop not found"}), 404

    return jsonify({
        "crop": crop_name,
        "price": crop["price"],
        "demand": crop["demand"],
        "season": crop["season"],
    })


@app.route("/crop/<crop_name>")
def crop_details(crop_name):
    crop = CROP_INFO.get(crop_name)
    if crop is None:
        return jsonify({"error": "Crop not found"}), 404

    return jsonify({"name": crop_name, **crop})


if __name__ == "__main__":
    app.run(debug=True)
