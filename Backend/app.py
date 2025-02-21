from flask import Flask, jsonify, request
from basic import train_initial_model, predict_sales, add_data, retrain_model, model_path, load_model
import os
from basic import train_initial_model, predict_sales, add_data, retrain_model, model_path, scaler
import tensorflow as tf 
from tensorflow.keras.models import load_model
from joblib import load
from basic import*
tf.config.run_functions_eagerly(True)

app = Flask(__name__)

# Check if model exists, otherwise train it
if not os.path.exists(model_path) or not os.path.exists("scaler.pkl"):
    print("Training model from scratch...")
    train_initial_model()
else:
    print("Loading existing model and scaler")
    
    model = load_model(model_path,custom_objects={"mse":tf.keras.losses.MeanSquaredError()})
    scaler = load("scaler.pkl")
    from basic import model as basic_model, scaler as basic_scaler
    basic_model = model
    basic_scaler = scaler

# Flask endpoint to train the model
@app.route("/train", methods=["POST"])
def train():
    try:
        train_initial_model()
        return jsonify({"message": "Model trained successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Flask endpoint to predict sales and allocate shelf space
@app.route("/predict", methods=["GET"])
def predict():
    try:
        results = predict_sales()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Flask endpoint to add new data
@app.route("/add-data", methods=["POST"])
def add_new_data():
    try:
        new_data = request.get_json()
        message = add_data(new_data)
        return jsonify({"message": message}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Flask endpoint to retrain the model incrementally
@app.route("/retrain", methods=["POST"])
def retrain():
    try:
        message = retrain_model()
        return jsonify({"message": message}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/profit_by_item', methods=['GET'])
def profit_by_item():
  try:  
    items = extract_item_data()
    img = generate_profit_by_item_graph(items)
    return send_file(img, mimetype='image/png')
  except Exception as e:
        return jsonify({"error": str(e)}), 500  


@app.route('/frequency_of_sale', methods=['GET'])
def frequency_of_sale():
   try: 
    items = extract_item_data()
    img = generate_frequency_of_sale_graph(items)
    return send_file(img, mimetype='image/png')
   except Exception as e:
        return jsonify({"error": str(e)}), 500          

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
