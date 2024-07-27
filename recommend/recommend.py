# recommendation_system.py

import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='static')

# Load and preprocess data
def load_data():
    # Replace with the path to your dataset
    data = pd.read_csv('data/dataset.csv')
    return data

def get_recommendations(category, data):
    # Filter products based on the given category
    recommendations = data[data['CATEGORY'] == category]
    
    # Drop duplicates and reset index
    recommendations = recommendations.drop_duplicates(subset='PRODUCT').reset_index(drop=True)
    
    # Return list of recommended products
    return recommendations['PRODUCT'].tolist()

@app.route('/recommend', methods=['GET'])
def recommend():
    category = request.args.get('category')
    data = load_data()
    recommendations = get_recommendations(category, data)
    return jsonify(recommendations)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
