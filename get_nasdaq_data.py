import os
import requests
import pandas as pd
import time

from dotenv import load_dotenv
from datetime import datetime, timedelta
import plotly.graph_objs as go


STOCKS = {
    "Adobe Inc.": "ADBE",
    "Advanced Micro Devices": "AMD",
    "Alexion Pharmaceuticals": "ALXN",
    "Align Technology": "ALGN",
    "Amazon.com": "AMZN",
    "American Electric Power": "AEP",
    "Apple Inc.": "AAPL",
    "Baidu": "BIDU",
    "Broadcom Inc.": "AVGO",
    "DexCom": "DXCM"}


def download_and_save_nasdaq_df(company_name):
    load_dotenv()
    alpha_vantage_url = os.getenv("STOCK_URL").format(company_name=company_name)
    response = requests.get(alpha_vantage_url)

    if "Thank you for using Alpha Vantage!" in response.text:
        time.sleep(60)
        return download_and_save_nasdaq_df(company_name)

    nasdaq_df = pd.DataFrame([x.split(',') for x in response.text.split('\r\n')])
    nasdaq_df.columns = nasdaq_df.loc[0]
    nasdaq_df = nasdaq_df.loc[1:]
    nasdaq_df.timestamp = pd.to_datetime(nasdaq_df.timestamp)
    date_filter = (datetime(datetime.today().year, datetime.today().month, 1) > nasdaq_df['timestamp']) & \
                  (nasdaq_df['timestamp'] > datetime.now() - timedelta(days=365))

    nasdaq_df['name'] = company_name
    current_path = os.path.dirname(os.path.abspath(__file__))
    nasdaq_df[date_filter].reset_index(drop=True).to_csv(fr'{current_path}\data\nasdaq\company_data_{company_name}.csv')


def get_companies_df():
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.listdir(fr'{current_path}\data\nasdaq')
    return [pd.read_csv(fr'{current_path}\data\nasdaq\{path}') for path in data_path]


def nasdaq_data_maker():
    data = []

    general_nasdaq_df = None
    companies_df = get_companies_df()

    for company_df in companies_df:
        if general_nasdaq_df is None:
            general_nasdaq_df = company_df
        else:
            general_nasdaq_df.append(company_df)

        data.append(go.Scatter(x=company_df.timestamp,
                               y=company_df.volume,
                               hovertext=company_df,
                               name=company_df.name.loc[0],
                               showlegend=True))
    return data, general_nasdaq_df
