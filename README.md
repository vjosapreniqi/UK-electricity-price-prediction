# UK-electricity-price-prediction

ARIMA Models: This file contains different statistical time-series tests components such as Stationarity, Autocorrelation and Partial Autocorrelation and ARIMA Models. Also, auto_arima is used besides other manually adjusted models.
The Prophet Models: This file contains only prophet models build for the electricity price prediction.
The XGBoost Models: This file contains only XGBboost algorithm with feature importance and other adjustments used for the task.
EDA and all forecasting models: this file contains Exploratory Data Analysis and three proposed models, all-together.
MID-preprocessing: This file contains data cleansing, adjusting and the application of feature engineering.
INDO-preprocessing: This file contains the preprocessing steps done on the load demand data after extracting from the Elexon API
INDO-models: this file contains 2 prediction models for national demand

Datasets:
2017-2019-mid.csv: The original Market Index Data taken from the Elexon API
mid-2017-2019-datetime.csv: The Market Index Data with added feature engineering
gas_data.csv: Gas Prices dataset 
INDO-2017-2019.csv: Initial National Demand Out-turn Data 
ITSDO-2017-2019.csv: Initial Transmission Demand Out-turn Data
Initial-Demand-Outturn.csv: INDO + ITSDO originally as extracted from the Elexon API
mid-gas-2017-2019.csv: The two datasets MID+Gas prices merged into one dataset
generated_holidays.csv: The dataset of the holidays taken by Facebook Prophet Model Source
If you want to get the data for different periods, you can use this pdf link for the dataset 5.2.8 Market Index Data and use APIconnection code in python:

https://www.elexon.co.uk/wp-content/uploads/2017/06/bmrs_api_data_push_user_guide_v1.1.pdf
