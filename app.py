import json
from datetime import datetime
import requests
import plotly.graph_objs as go
import plotly.express as px
import plotly
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     symbol = 'BTCUSDT'
#     interval = '1m'
#     limit = 30
#     url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
#     response = requests.get(url)
#     data = response.json()
#     x = []
#     open_values = []
#     high_values = []
#     low_values = []
#     close_values = []
#     for candle in data:
#         x.append(datetime.fromtimestamp(candle[0]/1000))
#         open_values.append(candle[1])
#         high_values.append(candle[2])
#         low_values.append(candle[3])
#         close_values.append(candle[4])
#     candlestick = go.Candlestick(x=x, open=open_values, high=high_values, low=low_values, close=close_values)
#     data = [candlestick]
#     layout = go.Layout(title=symbol)
#     fig = go.Figure(data=data, layout=layout)
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return render_template('index.html', graphJSON=graphJSON)
# if __name__ == '__main__':
#     app.run(debug=True)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        open_price = request.form['open']
        high_price = request.form['high']
        low_price = request.form['low']
        close_price = request.form['close']
        print(f"{date}, {open_price}, {high_price}, {low_price}, {close_price}")
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    symbol = 'BTCUSDT'
    interval = '1m'
    limit = 30
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
