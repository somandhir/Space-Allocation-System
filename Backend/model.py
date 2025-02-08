from pymongo import MongoClient
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import os

# Define model path
model_path = "sales_model.h5"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["store_sales"]
collection = db["sales_data"]



# Function to fetch and preprocess data
def get_training_data():
    data = list(collection.find())
    if not data:
        print("No data in MongoDB!")
        return None, None
    extracted_data=[]    
   #conversion to pandas dataframe
    for record in data:
      for key,value in record.items():
        if key.startswith("item_") and isinstance(value, dict):
            
            if all(k in value for k in ["buy", "time", "profit", "name"]):

                extracted_data.append(value)
    if not extracted_data:
        print("No valid data in MongoDB!")
        return None, None            

    df=pd.DataFrame(extracted_data)
    required_columns = ["buy", "time", "profit", "name"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {', '.join(missing_columns)}")
        return None, None       
    
    X=df[["buy", "time", "profit", "name"]]
    y=df["profit"]
    
    
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

   
    
    return X_scaled, y

# Function to build and train the model
def train_model():
    X, y = get_training_data()
    
    if X is None:
        print("No training data available.")
        return
    
    # Define neural network model
    model = Sequential([
        Dense(128, activation='relu', input_dim=X.shape[1]),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dense(1)  # Output layer
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    # Train the model
    model.fit(X, y, epochs=50, batch_size=16, verbose=1)
    
    # Save the trained model
    model.save(model_path)
    print(f"Model trained and saved at {model_path}")

# Check if model exists, otherwise train it
if not os.path.exists(model_path):
    print("Training model from scratch...")
    train_model()
else:
    print(f"Model already exists at {model_path}")