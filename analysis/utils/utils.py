import math
import time
import numpy as np
import pandas as pd
from copy import copy
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from tensorflow.keras import backend as K

def load_data(lookback_window, city):
    labels = pd.read_csv('../data/dengue_labels_train.csv', parse_dates=True)
    features = pd.read_csv('../data/dengue_features_train.csv', parse_dates=True)

    all_data = pd.merge(labels, features, on=['city', 'year', 'weekofyear'])
    city_data = all_data[all_data.city == city]
    df = city_data.drop(['city', 'week_start_date'], axis=1)
    df = df.reset_index()
    df = df.drop(['index'], axis=1).sort_values(['year', 'weekofyear'], ascending=[True, True])

    # Move "total_cases" to column 0 to avoid bugs
    cols = list(df)
    cols.insert(0, cols.pop(cols.index('total_cases')))
    df = df.loc[:, cols]

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    return df

def normalize_data(df):
    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler.fit(x)
    x_scaled = min_max_scaler.transform(x)
    df = pd.DataFrame(x_scaled, columns=df.columns)
    return df

def format_data(df, lookback_window=12, only_features=False, to_drop=['total_cases'], lstm=False):
    x = []
    y = []
    x_data = df.copy()
    
    if only_features:
        x_data = x_data.drop(to_drop, axis=1)

    for i in range(len(df)-lookback_window):
        x_entry = copy(x_data[i:i+lookback_window].values.T) # include current value
        
        if not only_features:
            x_entry[0][lookback_window-1] = 0.0 # erase variable to be predicted
        
        x.append(x_entry)
        y_entry = df['total_cases'][i+lookback_window-1]
        y.append(y_entry)
        
    x = np.array(x)
    y = np.array(y)
    return x, y

def split_data(x, y, val_size):
    train_size = len(x)-val_size
    x_train, y_train = x[0:train_size], y[0:train_size]
    x_val, y_val = x[train_size:train_size+val_size], y[train_size:train_size+val_size]
    
    assert y_train.shape[0]+y_val.shape[0] == len(y)
    
    return x_train, y_train, x_val, y_val


def train_model(model, data, epochs=200, plot=True, verbose=False):
    start_time = time.time()
    print('Training...')
    x_train, y_train, x_val, y_val = data
    validation_data = (x_val, y_val)
    history = model.fit(x_train, y_train, epochs=epochs,
                        verbose=verbose, validation_data=validation_data, batch_size=50)
    elapsed_time = time.time() - start_time
    
    print("Elapsed Time: {}".format(elapsed_time))
    
    if plot:
        plt.plot(history.history['loss'], label='train')
        plt.plot(history.history['val_loss'], label='validation')
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(loc='upper right')
        plt.show()
        
def plot_train_val(model, data):
    x_train, y_train, x_val, y_val = data
    p = model.predict(x_train)
    plt.plot(y_train, label='actual')
    plt.plot(p, label='predicted')
    plt.title('Weekly Dengue Cases')
    plt.legend()
    plt.show()

    p = model.predict(x_val)
    plt.plot(y_val, label='actual')
    plt.plot(p, label='predicted')
    plt.title('Weekly Dengue Cases')
    plt.legend()
    plt.show()

    
def forecast(model, forecast_window, last_train, test_data):
    lookback_window = last_train.shape[1]
    current = np.expand_dims(last_train, axis=0)
    next_y = model.predict(current)[0][0]
    current[0][0][-1] = next_y
    
    result = []
    for xi in test_data:
        xi[0][0:lookback_window] = current[0][0][-lookback_window:]
        current = np.expand_dims(xi, axis=0)
        next_y = model.predict(current)[0][0]
        current[0][0][-1] = next_y
        result.append(next_y)
    
    return result
    
def fake_test_data(x_val):
    x_test = copy(x_val)
    for i in x_test:
        i[0] = 0.0
    return x_test

def forecast_analysis(model, data):
    x_train, y_train, x_val, y_val = data
    x_test = fake_test_data(x_val)
    result = forecast(model, len(x_test), copy(x_train[-1]), x_test) 
    
    error = mean_absolute_error(y_val, result)
    print("Forecast MAE: {}".format(error))

    plt.plot(y_val, label='actual')
    plt.plot(result, label='forecast')
    plt.title('Weekly Dengue Cases Forecasting')
    plt.legend()
    plt.show()
    return result
    

def experiment(model_fn, hyperp):
    K.clear_session()
    
    # Load and format_data
    df = load_data(hyperp['lookback_window'], city= hyperp['city'])
    if 'normalize' in hyperp and hyperp['normalize']:
        df = normalize_data(df)
    
    x, y = format_data(df, hyperp['lookback_window'])
    val_size = int(math.floor((len(x)*(1-hyperp['train_split_percent']))))
    x_train, y_train, x_val, y_val = split_data(x, y, val_size)
    data = x_train, y_train, x_val, y_val
    
    # Train Model
    input_shape = (x.shape[1], x.shape[2])
    model = model_fn(input_shape)
    train_model(model, data, epochs=hyperp['epochs'], verbose=hyperp['verbose'])
    plot_train_val(model, data)
    df_results = forecast_analysis(model, data)
    return df_results
    