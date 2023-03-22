from datetime import datetime
import requests
from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import numpy as np

app = Flask(__name__)

close_values = []
open_price = 0
high_price = 0
low_price = 0
volumeto = 0
volumefrom = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    # load tensorflow model
    model = tf.keras.models.load_model('btc_model.h5')

    # Handle form submission
    if request.method == 'POST':        
        date = request.form['date']       
        scaler = MinMaxScaler()
        date_ordinal = datetime.strptime(date, '%Y-%m-%d').toordinal()
        features = [[high_price, low_price, open_price, volumefrom, volumeto, date_ordinal]]        
        features_scaled = scaler.fit_transform(features)        
        # Make prediction using model
        prediction = model.predict(features_scaled)
        close_values_scaled = scaler.fit_transform(np.array(close_values).reshape(-1, 1))
        prediction = close_values_scaled[-1] + prediction
        prediction = scaler.inverse_transform(prediction)
        prediction = prediction[0][0]
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    symbol = 'BTCUSDT'
    interval = '1m'
    limit = 30
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    for candle in response.json():
        close_values.append(candle[4])
        open_price = candle[1]
        high_price = candle[2]
        low_price = candle[3]
        volumeto = candle[5]
        volumefrom = candle[7]
        
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
