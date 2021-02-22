import os
import requests
import pandas as pd
import time

from dotenv import load_dotenv
from datetime import datetime, timedelta

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


def download_and_save_company_df(company_name):
    load_dotenv()
    alpha_vantage_url = os.getenv("CSV_URL").format(company_name=company_name)
    response = requests.get(alpha_vantage_url)

    if "Thank you for using Alpha Vantage!" in response.text:
        time.sleep(60)
        return download_and_save_company_df(company_name)

    df = pd.DataFrame([x.split(',') for x in response.text.split('\r\n')])
    df.columns = df.loc[0]
    df = df.loc[1:]
    df.timestamp = pd.to_datetime(df.timestamp)
    date_filter = (datetime(datetime.today().year, datetime.today().month, 1) > df['timestamp']) & \
                  (df['timestamp'] > datetime.now() - timedelta(days=365))

    df['name'] = company_name
    current_path = os.path.dirname(os.path.abspath(__file__))
    df[date_filter].reset_index(drop=True).to_csv(f'{current_path}\data\company_data_{company_name}.csv')


def get_companies_df():
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.listdir(f'{current_path}\data')
    return [pd.read_csv(f'{current_path}\data\{path}') for path in data_path]
