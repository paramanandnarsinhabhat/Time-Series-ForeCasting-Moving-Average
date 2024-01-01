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

