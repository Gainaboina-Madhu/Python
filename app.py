from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load models
nb_model = pickle.load(open("Nb.pkl", "rb"))
knn_model = pickle.load(open("Knn.pkl", "rb"))

# Class labels
classes = ["Setosa", "Versicolor", "Virginica"]


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Predict route
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from form
        sl = float(request.form["sl"])
        sw = float(request.form["sw"])
        pl = float(request.form["pl"])
        pw = float(request.form["pw"])
        model_name = request.form["model"]

        # Convert to numpy array
        features = np.array([[sl, sw, pl, pw]])

        # Select model
        if model_name == "nb":
            prediction = nb_model.predict(features)[0]
        else:
            prediction = knn_model.predict(features)[0]

        result = classes[int(prediction)]

        return render_template(
            "index.html",
            prediction_text=f"Prediction: {result} using {model_name.upper()}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


# Run app
if __name__ == "__main__":
    app.run(debug=True)