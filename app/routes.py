from flask import Blueprint, request, jsonify
from .model_loader import load_model, predict_probability

# Blueprint for API routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return "Welcome to the Cricket Match Predictor API!"

@api_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Expected columns
        columns = ['BattingTeam', 'BowlingTeam', 'City', 'runs_left', 'balls_left',
                   'wickets_left', 'current_run_rate', 'required_run_rate', 'target']

        # Validate and predict
        try:
            prediction = predict_probability(data, columns)
            return jsonify(prediction)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
