import os
import requests
import pandas as pd
import time

from datetime import datetime, timedelta
import plotly.graph_objs as go


CRYPTOS = {
    "Ethereum": "ETH",
    "Litecoin": "LTC",
    "Cardano": "ADA",
    "Polkadot": "DOT",
    "Bitcoin Cash": "BCH",
    "Stellar": "XLM",
    "Bitcoin": "BTC",
    "Binance Coin": "BNB",
    "Ripple": "XRP",
    "Monero": "XMR"}


def download_and_save_crypto_df(crypto_name):
    alpha_vantage_url = os.getenv("CRYPTO_URL").format(crypto_name=crypto_name)
    response = requests.get(alpha_vantage_url)

    if "Thank you for using Alpha Vantage!" in response.text:
        time.sleep(60)
        return download_and_save_crypto_df(crypto_name)

    crypto_df = pd.DataFrame([x.split(',') for x in response.text.split('\r\n')])
    crypto_df.columns = crypto_df.loc[0]
    crypto_df = crypto_df.loc[1:]
    crypto_df.timestamp = pd.to_datetime(crypto_df.timestamp)
    date_filter = (datetime(datetime.today().year, datetime.today().month, 1) > crypto_df['timestamp']) & \
                  (crypto_df['timestamp'] > datetime.now() - timedelta(days=365))

    crypto_df['name'] = crypto_name
    current_path = os.path.dirname(os.path.abspath(__file__))
    crypto_df[date_filter].reset_index(drop=True).to_csv(fr'{current_path}\data\crypto\crypto_data_{crypto_name}.csv')


def get_crypto_df():
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.listdir(fr'{current_path}\data\crypto')
    return [pd.read_csv(fr'{current_path}\data\crypto\{path}') for path in data_path]


def crypto_data_maker():
    data = []

    general_crypto_df = None
    cryptos_df = get_crypto_df()

    for crypto_df in cryptos_df:
        if general_crypto_df is None:
            general_crypto_df = crypto_df
        else:
            general_crypto_df.append(crypto_df)

        data.append(go.Scatter(x=crypto_df.timestamp,
                               y=crypto_df.volume,
                               hovertext=crypto_df,
                               name=crypto_df.name.loc[0],
                               showlegend=True))
    return data, general_crypto_df
