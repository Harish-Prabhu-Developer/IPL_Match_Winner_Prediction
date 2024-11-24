import joblib
import pandas as pd

# Load the model
model_path = 'models/pipeRandomForest.pkl'
model = None

def load_model():
    global model
    if not model:
        model = joblib.load(model_path)
    return model

def predict_probability(data, expected_columns):
    # Ensure the model is loaded
    model = load_model()

    # Create a DataFrame
    try:
        input_data = pd.DataFrame([data], columns=expected_columns)
    except KeyError as e:
        raise ValueError(f"Missing key in input data: {str(e)}")

    # Predict probabilities
    probabilities = model.predict_proba(input_data).tolist()

    # Response
    return {
        "Team1_Probability": probabilities[0][0],
        "Team2_Probability": probabilities[0][1]
    }
