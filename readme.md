
# Time Series Forecasting with Moving Average

This repository contains a time series forecasting model that utilizes the Moving Average method. The model is applied to a dataset with the aim of predicting future values based on historical data trends.

## Overview

The Moving Average method is a time-honored technique used in time series analysis to smooth out short-term fluctuations and highlight longer-term trends or cycles. This project implements a simple Moving Average forecast to provide insights and predictions based on the provided data.

## Dataset

The project uses two datasets: `train_data.csv` for training and `valid_data.csv` for validation. The datasets include a series of observations over time, which are used to forecast future values.

## Requirements

To run this project, the following Python libraries are needed:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For plotting and visualization.
- `scikit-learn`: For calculating the root mean square error (RMSE).

## Structure

The project has the following structure:

```
TIME-SERIES-FORECASTING/
│
├── data/
│   ├── train/
│   └── valid/
│
├── myenv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── share/
│
├── notebook/
│   └── Moving Average.ipynb
│
├── scripts/
│   └── time_series_moving_average.py
│
├── .gitignore
├── readme.md
└── requirements.txt
```

## Implementation

The forecasting process involves several key steps:
1. Loading and preprocessing the data, including parsing dates and setting them as DataFrame indices.
2. Visualizing the training and validation data to understand underlying patterns.
3. Implementing the Moving Average forecast by maintaining a list of the last seven observations and predicting the next value as the mean of these observations.
4. Plotting the forecasted values alongside the actual data for comparison.
5. Computing the RMSE to quantify the forecast accuracy.

## Running the Project

To run the project, make sure you have activated your Python environment and installed all the dependencies listed in `requirements.txt`. Then, navigate to the `scripts` directory and run the `time_series_moving_average.py` script.

## Visualization

The repository includes a Jupyter notebook (`Moving Average.ipynb`) that contains visualizations of the Moving Average forecasts compared to the actual data.

## Contributions

Contributions, bug reports, and feature requests are welcome. Feel free to submit issues or pull requests in this repository.

## License

This project is open-sourced under the MIT License.

