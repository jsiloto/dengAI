import math
import time
import numpy as np
import pandas as pd
from copy import copy
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from tensorflow.keras import backend as K

def split_data(x, y, val_size):
    train_size = len(x)-val_size
    x_train, y_train = x[0:train_size], y[0:train_size]
    x_val, y_val = x[train_size:train_size+val_size], y[train_size:train_size+val_size]
    assert y_train.shape[0]+y_val.shape[0] == len(y)
    return x_train, y_train, x_val, y_val

    
def fake_test_data(x_val):
    x_test = copy(x_val)
    for i in x_test:
        i[0] = 0.0
    return x_test

class Experiment(object):
    
    def __init__(self, model_fn, hyperparameters):
        self.epochs = hyperparameters.get('epochs', 100)
        self.train_split_percent = hyperparameters.get('train_split_percent', 70)
        self.lookback_window = hyperparameters.get('lookback_window', 100)
        self.verbose = hyperparameters.get('verbose', False)
        self.plot = hyperparameters.get('plot', True)
        self.normalize = hyperparameters.get('normalize', False)
        self.only_features = hyperparameters.get('only_features', False)
        self.lr = hyperparameters.get('lr', 1e-5)
        self.city = hyperparameters['city']
        self.model_fn = model_fn
        self.y_scaler = None
        self.model = None
        
    def load_data(self):
        labels = pd.read_csv('../data/dengue_labels_train.csv', parse_dates=True)
        features = pd.read_csv('../data/dengue_features_train.csv', parse_dates=True)
    
        all_data = pd.merge(labels, features, on=['city', 'year', 'weekofyear'])
        city_data = all_data[all_data.city == self.city]
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

    def normalize_data(self, df):
        x = df.values #returns a numpy array
        y = df['total_cases'].values
        
        min_max_scaler = preprocessing.MinMaxScaler()
        min_max_scaler.fit(x)
        x_scaled = min_max_scaler.transform(x)
        df = pd.DataFrame(x_scaled, columns=df.columns)
        
        y_scaler = preprocessing.MinMaxScaler()
        y_scaler.fit(y.reshape(-1, 1))
        
        return y_scaler, df

    def format_data(self, df, to_drop=['total_cases']):
        x = []
        y = []
        x_data = df.copy()
        
        if self.only_features:
            x_data = x_data.drop(to_drop, axis=1)
    
        for i in range(len(df)-self.lookback_window):
            x_entry = copy(x_data[i:i+self.lookback_window].values.T) # include current value
            
            if not self.only_features:
                x_entry[0][self.lookback_window-1] = 0.0 # erase variable to be predicted
            
            x.append(x_entry)
            y_entry = df['total_cases'][i+self.lookback_window-1]
            y.append(y_entry)
            
        x = np.array(x)
        y = np.array(y)
        return x, y

    def train_model(self, model, data):
        start_time = time.time()
        print('Training...')
        x_train, y_train, x_val, y_val = data
        validation_data = (x_val, y_val)
        history = model.fit(x_train, y_train, epochs=self.epochs,
                            verbose=self.verbose, validation_data=validation_data, batch_size=50)
        elapsed_time = time.time() - start_time
        print("Elapsed Time: {}".format(elapsed_time))
        
        if self.plot:
            plt.plot(history.history['loss'], label='train')
            plt.plot(history.history['val_loss'], label='validation')
            plt.title('model loss')
            plt.ylabel('loss')
            plt.xlabel('epoch')
            plt.legend(loc='upper right')
            plt.show()
        
    def analysis_train_val(self, model, data):
        x_train, y_train, x_val, y_val = data
        p = model.predict(x_train)
        if self.normalize:
            y_train = self.y_scaler.inverse_transform(y_train.reshape(1, -1)).reshape(-1)
            p = self.y_scaler.inverse_transform(p.reshape(1, -1)).reshape(-1)
        train_error = mean_absolute_error(y_train, p)
        print("Train MAE: {}".format(train_error))
        if self.plot:
            plt.plot(y_train, label='actual')
            plt.plot(p, label='predicted')
            plt.title('Weekly Dengue Cases')
            plt.legend()
            plt.show()
    
        p = model.predict(x_val)
        if self.normalize:
            y_val = self.y_scaler.inverse_transform(y_val.reshape(1, -1)).reshape(-1)
            p = self.y_scaler.inverse_transform(p.reshape(1, -1)).reshape(-1)
        val_error = mean_absolute_error(y_val, p)
        print("Validation MAE: {}".format(val_error))
        if self.plot:
            plt.plot(y_val, label='actual')
            plt.plot(p, label='predicted')
            plt.title('Weekly Dengue Cases')
            plt.legend()
            plt.show()
        
        return train_error, val_error

    
    def forecast(self, model, last_train, test_data):
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
        
        return np.array(result)


    def forecast_analysis(self, model, data):
        x_train, y_train, x_val, y_val = data
        x_test = fake_test_data(x_val)
        result = self.forecast(model, copy(x_train[-1]), x_test) 
        
        if self.normalize:
            y_val = self.y_scaler.inverse_transform(y_val.reshape(1, -1)).reshape(-1)
            result = self.y_scaler.inverse_transform(result.reshape(1, -1)).reshape(-1)
        
        
        forecast_error = mean_absolute_error(y_val, result)
        print("Forecast MAE: {}".format(forecast_error))
        if self.plot:
            plt.plot(y_val, label='actual')
            plt.plot(result, label='forecast')
            plt.title('Weekly Dengue Cases Forecasting')
            plt.legend()
            plt.show()
        return forecast_error
    
    def forecast_on_test_data(self, model, df_train_val):
        labels = pd.read_csv('../data/submission_format.csv', parse_dates=True)
        features = pd.read_csv('../data/dengue_features_test.csv', parse_dates=True)
    
        df_test = pd.merge(labels, features, on=['city', 'year', 'weekofyear'])
    
        df_test = df_test[df_test.city == self.city]
        df_test = df_test.drop(['city', 'week_start_date'], axis=1)
        len_test = len(df_test)
        
        df_full = pd.concat([df_train_val, df_test], sort=False)
        df_full = df_full.reset_index()
        df_full = df_full.drop(['index'], axis=1).sort_values(['year', 'weekofyear'], ascending=[True, True])
        df_full.fillna(method='ffill', inplace=True)
        df_full.fillna(method='bfill', inplace=True)
    
        # Ensure the same order of columns
        cols = list(df_train_val)
        cols.insert(0, cols.pop(cols.index('total_cases')))
        df_full = df_full.loc[:, cols]
        
        x, y = self.format_data(df_full)
        x_train, y_train, x_test, y_test = split_data(x, y, len_test)
        result = self.forecast(model, copy(x_train[-1]), x_test)
        
        if self.normalize:
            y_train = self.y_scaler.inverse_transform(y_train.reshape(1, -1)).reshape(-1)
            result = self.y_scaler.inverse_transform(result.reshape(1, -1)).reshape(-1)
        
        if self.plot:
            plt.plot(y_train, label='known')
            plt.plot(range(len(y_train), len(y_train)+len(result)), result, label='forecast')
            plt.title('Weekly Dengue Cases Forecasting')
            plt.legend()
            plt.show()
        
        df_results = labels[labels.city == self.city].reset_index()
        df_results['total_cases'] = np.round(np.array(result)).astype(int)
        return df_results.drop(['index'], axis=1)
    
    
    def run(self):
        K.clear_session()

        # Load and format_data
        df = self.load_data()
        if self.normalize:
            print("Normalizing Features!")
            self.y_scaler, df = self.normalize_data(df)
        
        x, y = self.format_data(df)
        val_size = int(math.floor((len(x)*(1-self.train_split_percent))))
        x_train, y_train, x_val, y_val = split_data(x, y, val_size)
        data = x_train, y_train, x_val, y_val
        
        # Train Model
        input_shape = (x.shape[1], x.shape[2])
        self.model = self.model_fn(input_shape, self.lr)
        self.train_model(self.model, data)
        train_error, val_error = self.analysis_train_val(self.model, data)
        forecast_error = self.forecast_analysis(self.model, data)
        df_results = self.forecast_on_test_data(self.model, df)
        
        return (train_error, val_error, forecast_error), df_results
    