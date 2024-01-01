import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 

import warnings
warnings.filterwarnings("ignore")


train_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.3_and_4.4_-_MA_and_WMA/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.3_and_4.4_-_MA_and_WMA/data/valid_data.csv")

print(train_data.shape)
print(train_data.head())

print(valid_data.shape)
print(valid_data.head())


#Required Preprocessing
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp

valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.legend(loc='best')
plt.title("Train and Validation Data")
plt.show()




# list holding last seven values

valid_data['moving_average'] = 0
week_values = [192, 124, 149, 129, 119, 214, 236]

for i in range(0,len(valid_data)):
    end = len(week_values)
    start = len(week_values)-7
    pred = mean(week_values[start:end])
    
    valid_data['moving_average'][i] = pred
    week_values.append(pred)

plt.figure(figsize=(12,8))
plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.plot(valid_data.index,valid_data['moving_average'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.title("Moving Average Method")
plt.show()

# calculating RMSE 
rmse = sqrt(mean_squared_error(valid_data['count'], valid_data['moving_average']))
print('The RMSE value for Moving Approach is', rmse)