# UK-electricity-price-prediction

This repository represents the UK electricity price prediction utilising 3 Machine Learning learning Models:
1. ARIMA Models
2. Prophet Model
3. XGBoost Model.
The Data is extracted from the ELEXON open source API:https://www.elexon.co.uk/wp-content/uploads/2017/06/bmrs_api_data_push_user_guide_v1.1.pdf
The period captured in this repository for the electricity prices is 01/01/2017 - 01/07/2019.

# Technical info:

Each Model is saved in separately into jupiter notebooks and can be found in the Nooteooks folder.
- ARIMA Models.ipynb contains different statistical time-series tests components such as Stationarity, Autocorrelation and Partial Autocorrelation and ARIMA Models. Also, auto_arima is used besides other manually adjusted models.
- Prophet Models.ipynb contains prophet models build for the electricity price prediction.
- XGBoost Models.ipynb file contains XGBboost algorithm with feature importance and other adjustments used for the task.
- Exploratory Data Analysis file contains Exploratory Data Analysis and Visualistions for the datasets used for the project. 
- MID-preprocessing file contains data cleansing, adjusting and the application of feature engineering.
- INDO-preprocessin file contains the preprocessing steps done on the load demand data after extracting from the Elexon API
- INDO-models file contains 2 prediction models for national demand

Datasets:
Can be found within csv-files folder.
- 2017-2019-mid.csv: The original Market Index Data taken from the Elexon API
- mid-2017-2019-datetime.csv: The Market Index Data with added feature engineering
- gas_data.csv: Gas Prices dataset 
- INDO-2017-2019.csv: Initial National Demand Out-turn Data 
- ITSDO-2017-2019.csv: Initial Transmission Demand Out-turn Data
- Initial-Demand-Outturn.csv: INDO + ITSDO originally as extracted from the Elexon API
- mid-gas-2017-2019.csv: The two datasets MID+Gas prices merged into one dataset
- generated_holidays.csv: The dataset of the holidays taken by Facebook Prophet Model Source

# Prerequisites
- Clone repository:
`git clone https://github.com/vjosapreniqi/UK-electricity-price-prediction.git`

- Install the requirements
`pip install -r ./requirements.txt`