from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("pipeRandomForest.pkl")

@app.route('/')
def home():
    return "Welcome to the Cricket Match Predictor API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Expected columns
        columns = ['BattingTeam', 'BowlingTeam', 'City', 'runs_left', 'balls_left',
                   'wickets_left', 'current_run_rate', 'required_run_rate', 'target']

        # Validate and create a DataFrame
        try:
            team2023 = pd.DataFrame([data], columns=columns)
        except KeyError as e:
            return jsonify({"error": f"Missing key in input data: {str(e)}"}), 400

        # Predict the probability
        probabilities = model.predict_proba(team2023).tolist()

        # Get the prediction result (win probability for both teams)
        response = {
            "Team1_Probability": probabilities[0][0],  # Losing probability
            "Team2_Probability": probabilities[0][1]   # Winning probability
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
