from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)
CORS(app)


# =========================================================
# FILE NAMES
# =========================================================

MODEL_FILE = "heart_model.pkl"
SCALER_FILE = "scaler.pkl"
RECORD_FILE = "prediction_records.csv"


# =========================================================
# LOAD MODEL
# =========================================================

try:
    model = joblib.load(MODEL_FILE)
    print("Heart disease model loaded successfully!")

except Exception as e:
    model = None
    print("Model loading error:", e)


# =========================================================
# LOAD SCALER
# =========================================================

try:
    scaler = joblib.load(SCALER_FILE)
    print("Scaler loaded successfully!")

except Exception as e:
    scaler = None
    print("Scaler loading error:", e)


# =========================================================
# CREATE RECORD FILE
# =========================================================

def create_record_file():

    if not os.path.exists(RECORD_FILE):

        columns = [
            "Date & Time",
            "Age",
            "Gender",
            "Height",
            "Weight",
            "Systolic BP",
            "Diastolic BP",
            "Cholesterol",
            "Glucose",
            "Smoking",
            "Alcohol",
            "Physical Activity",
            "Prediction",
            "Risk Probability"
        ]

        df = pd.DataFrame(columns=columns)

        df.to_csv(
            RECORD_FILE,
            index=False
        )


create_record_file()


# =========================================================
# HOME
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "status": "success",

        "message":
            "CardioAI Backend is running successfully!",

        "service":
            "Heart Disease Prediction API"

    })


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health", methods=["GET"])
def health():

    if model is not None and scaler is not None:

        return jsonify({

            "status": "healthy",

            "model": "loaded",

            "scaler": "loaded"

        })

    return jsonify({

        "status": "error",

        "model":
            "loaded" if model is not None
            else "not loaded",

        "scaler":
            "loaded" if scaler is not None
            else "not loaded"

    }), 500


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # -------------------------------------------------
        # GET JSON
        # -------------------------------------------------

        data = request.get_json()

        if not data:

            return jsonify({

                "success": False,

                "error":
                    "No data received"

            }), 400


        # -------------------------------------------------
        # GET VALUES
        # -------------------------------------------------

        age = float(data["age"])

        gender = float(data["gender"])

        height = float(data["height"])

        weight = float(data["weight"])

        ap_hi = float(data["ap_hi"])

        ap_lo = float(data["ap_lo"])

        cholesterol = float(
            data["cholesterol"]
        )

        gluc = float(
            data["gluc"]
        )

        smoke = float(
            data["smoke"]
        )

        alco = float(
            data["alco"]
        )

        active = float(
            data["active"]
        )


        # -------------------------------------------------
        # CHECK MODEL
        # -------------------------------------------------

        if model is None:

            return jsonify({

                "success": False,

                "error":
                    "Heart model is not loaded."

            }), 500


        # -------------------------------------------------
        # CHECK SCALER
        # -------------------------------------------------

        if scaler is None:

            return jsonify({

                "success": False,

                "error":
                    "Scaler is not loaded."

            }), 500


        # -------------------------------------------------
        # CREATE INPUT
        # -------------------------------------------------

        input_data = np.array([

            [
                age,
                gender,
                height,
                weight,
                ap_hi,
                ap_lo,
                cholesterol,
                gluc,
                smoke,
                alco,
                active
            ]

        ])


        # -------------------------------------------------
        # SCALE INPUT
        # -------------------------------------------------

        input_scaled = scaler.transform(
            input_data
        )


        # -------------------------------------------------
        # PREDICTION
        # -------------------------------------------------

        prediction = model.predict(
            input_scaled
        )[0]


        # -------------------------------------------------
        # PROBABILITY
        # -------------------------------------------------

        probability = None


        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_scaled
            )[0]


            # Find class 1 probability
            if hasattr(model, "classes_"):

                classes = list(
                    model.classes_
                )

                if 1 in classes:

                    class_index = classes.index(1)

                    probability = float(
                        probabilities[class_index] * 100
                    )

                else:

                    probability = float(
                        max(probabilities) * 100
                    )

            else:

                probability = float(
                    probabilities[-1] * 100
                )


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        if int(prediction) == 1:

            result = (
                "High Risk of Heart Disease"
            )

        else:

            result = (
                "Low Risk of Heart Disease"
            )


        # -------------------------------------------------
        # SAVE RECORD
        # -------------------------------------------------

        record = {

            "Date & Time":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                ),

            "Age":
                age,

            "Gender":
                "Female"
                if gender == 1
                else "Male",

            "Height":
                height,

            "Weight":
                weight,

            "Systolic BP":
                ap_hi,

            "Diastolic BP":
                ap_lo,

            "Cholesterol":
                cholesterol,

            "Glucose":
                gluc,

            "Smoking":
                smoke,

            "Alcohol":
                alco,

            "Physical Activity":
                active,

            "Prediction":
                result,

            "Risk Probability":
                round(
                    probability, 2
                )
                if probability is not None
                else None

        }


        record_df = pd.DataFrame(
            [record]
        )


        record_df.to_csv(

            RECORD_FILE,

            mode="a",

            header=False,

            index=False

        )


        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return jsonify({

            "success": True,

            "prediction":
                int(prediction),

            "result":
                result,

            "probability":
                round(
                    probability, 2
                )
                if probability is not None
                else None

        })


    # =====================================================
    # ERRORS
    # =====================================================

    except KeyError as e:

        return jsonify({

            "success": False,

            "error":
                f"Missing field: {str(e)}"

        }), 400


    except ValueError as e:

        return jsonify({

            "success": False,

            "error":
                f"Invalid value: {str(e)}"

        }), 400


    except Exception as e:

        return jsonify({

            "success": False,

            "error":
                str(e)

        }), 500


# =========================================================
# GET RECORDS
# =========================================================

@app.route("/records", methods=["GET"])
def get_records():

    try:

        create_record_file()

        df = pd.read_csv(
            RECORD_FILE
        )

        # Replace NaN with empty values
        df = df.fillna("")

        records = df.to_dict(
            orient="records"
        )

        return jsonify({

            "success": True,

            "records": records

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error":
                str(e)

        }), 500


# =========================================================
# DELETE ALL RECORDS
# =========================================================

@app.route("/records", methods=["DELETE"])
def delete_records():

    try:

        create_record_file()

        columns = [
            "Date & Time",
            "Age",
            "Gender",
            "Height",
            "Weight",
            "Systolic BP",
            "Diastolic BP",
            "Cholesterol",
            "Glucose",
            "Smoking",
            "Alcohol",
            "Physical Activity",
            "Prediction",
            "Risk Probability"
        ]

        empty_df = pd.DataFrame(
            columns=columns
        )

        empty_df.to_csv(
            RECORD_FILE,
            index=False
        )

        return jsonify({

            "success": True,

            "message":
                "All records deleted successfully."

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error":
                str(e)

        }), 500


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )