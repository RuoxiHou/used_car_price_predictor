from flask import Flask,render_template, request, jsonify, send_from_directory
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from category_encoders.target_encoder import TargetEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor
import pickle

# Load the dictionary from the pickle file
with open('car_data.pkl', 'rb') as f:
    car_data = pickle.load(f)
print(car_data)
# Load the prediction model from the pickle file
with open('xgb_reg_model.pkl', 'rb') as f:
    model = pickle.load(f)

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', car_data=car_data)

@app.route('/models')
def get_models():
    make = request.args.get('make')
    if make in car_data:
        models = list(car_data[make].keys())
        return jsonify(models)
    else:
        return jsonify([])
    
@app.route('/trims')
def get_trims():
    make = request.args.get('make')
    model = request.args.get('model')
    if make in car_data and model in car_data[make]:
        trims = car_data[make][model]
        return jsonify(trims)
    else:
        return jsonify([])
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        selected_make = request.form['selected_make']
        selected_model = request.form['selected_model']
        selected_trim = request.form['selected_trim']
        selected_fuel_type = request.form['selected_fuel_type']
        selected_body_type = request.form['selected_body_type']
        selected_transmission = request.form['selected_transmission']
        selected_euro_norm = request.form['selected_euro_norm']
        selected_country = request.form['selected_country']
        selected_color = request.form['selected_color']

        # Collect the input data into a DataFrame
        input_data = {
            'Make': [selected_make],
            'Model': [selected_model],
            'Trim': [selected_trim],
            'Fuel type': [selected_fuel_type],
            'Body type': [selected_body_type],
            'Transmission': [selected_transmission],
            'Emission standard': [selected_euro_norm],
            'Country': [selected_country],
            'Color': [selected_color],
            'Year': [int(request.form['year'])],
            'kW': [int(request.form['power_kw'])],
            'Mileage(km)': [int(request.form['mileage_km'])]
        }
        input_df = pd.DataFrame(input_data)

        # Make prediction using the model
        prediction = model.predict(input_df)

        return render_template('prediction.html', prediction=prediction)
    # For GET requests, simply render the form
    return render_template('index.html', car_data=car_data)

@app.route('/clear-form')
def clear_form():
    return redirect(url_for('index'))

@app.route('/market_overview')
def market_overview():
    return render_template('market_overview.html')

@app.route('/pipeline_xgb_reg')
def pipeline_xgb_reg():
    return render_template('pipeline_xgb_reg.html')

# Route to handle the request for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)