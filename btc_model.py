from tensorflow import keras
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=1000'
data = pd.read_json(url)
dataframe = pd.DataFrame(data['Data']['Data'])
data = dataframe[['time', 'high', 'low', 'open', 'volumefrom', 'volumeto']].copy()
data['date'] = pd.to_datetime(data['time'], unit='s').apply(lambda x: x.toordinal())
data.drop('time', axis=1, inplace=True)
data['close'] = dataframe[['close']]
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

x_train, y_train = train_data[:, :-1], train_data[:, -1]
x_test, y_test = test_data[:, :-1], test_data[:, -1]

model=keras.Sequential()
model.add(keras.layers.Dense(200, input_shape=(6,)))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1))
model.add(keras.layers.Activation('linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train model on training data
history_object=model.fit(x_train,y_train,
          epochs=20,
          batch_size=32,
          validation_split=0.2)

# Make predictions on test data
predictions = model.predict(x_test).squeeze()
mse = mean_squared_error(y_test,predictions)
r2 = r2_score(y_test,predictions)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
if r2 > 0.8:
    model.save('btc_model.h5')
