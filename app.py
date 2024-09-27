# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from dotenv import load_dotenv
from get_nasdaq_data import *
from get_crypto_data import *
from get_sector_data import *
from dash.dependencies import Input, Output
from threading import Thread

load_dotenv()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'My Sigma Project'
server = app.server



def drawer(figure_nasdaq_data=None, table_nasdaq_data=None, column_nasdaq_data=None,
           figure_crypto_data=None, table_crypto_data=None, column_crypto_data=None):
    colors = {
        'background': 'black',
        'text': 'white'}

    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold'
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#119DFF',
        'color': 'white',
        'padding': '6px'
    }

    if column_nasdaq_data is None:
        column_nasdaq_data = [{'id': 'timestamp', 'name': 'timestamp'},
                              {'id': 'open', 'name': 'open'},
                              {'id': 'high', 'name': 'high'},
                              {'id': 'low', 'name': 'low'},
                              {'id': 'close', 'name': 'close'},
                              {'id': 'volume', 'name': 'volume'},
                              {'id': 'name', 'name': 'name'}]

    if column_crypto_data is None:
        column_crypto_data = [{'id': 'timestamp', 'name': 'timestamp'},
                              {'id': 'open (CNY)', 'name': 'open(CNY)'},
                              {'id': 'high (CNY)', 'name': 'high(CNY)'},
                              {'id': 'low (CNY)', 'name': 'low(CNY)'},
                              {'id': 'close (CNY)', 'name': 'close(CNY)'},
                              {'id': 'open (USD)', 'name': 'open(USD)'},
                              {'id': 'high (USD)', 'name': 'high(USD)'},
                              {'id': 'low (USD)', 'name': 'low(USD)'},
                              {'id': 'close (USD)', 'name': 'close(USD)'},
                              {'id': 'volume', 'name': 'volume'},
                              {'id': 'market cap (USD)', 'name': 'market cap(USD)'},
                              {'id': 'name', 'name': 'name'}]

    fig1 = go.Figure(data=figure_nasdaq_data)
    fig1.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'])

    fig2 = go.Figure(data=figure_crypto_data)
    fig2.update_layout(plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'])

    fig3 = go.Figure(data=data_sectors)
    fig3.update_layout(barmode='group',
                       plot_bgcolor=colors['background'],
                       paper_bgcolor=colors['background'],
                       font_color=colors['text'])

    app.layout = html.Div(style={'backgroundColor': colors['background']},
                          children=[
                              html.H1(children='PYTHON PROJECT',
                                      style={
                                          'textAlign': 'center',
                                          'color': colors['text']}),

                              dcc.Tabs([
                                  dcc.Tab(label='NASDAQ INDEXES',
                                          style=tab_style,
                                          selected_style=tab_selected_style,
                                          children=[
                                              html.Button('Upload new data',
                                                          id='upload-nasdaq-button',
                                                          title='Upload most recent company data',
                                                          n_clicks=0,
                                                          style={
                                                              'backgroundColor': 'rgb(50, 50, 50)',
                                                              'color': 'white'}),

                                              html.Button('Draw a graphic',
                                                          id='draw-nasdaq-button',
                                                          title='Draw most recent company data',
                                                          n_clicks=0,
                                                          style={
                                                              'backgroundColor': 'rgb(50, 50, 50)',
                                                              'color': 'white'}),

                                              dcc.Graph(id='nasdaq-graph',
                                                        figure=fig1),

                                              dash_table.DataTable(id='datatable-nasdaq-interactivity',
                                                                   columns=column_nasdaq_data,
                                                                   data=table_nasdaq_data,
                                                                   editable=True,
                                                                   filter_action="native",
                                                                   sort_action="native",
                                                                   sort_mode="multi",
                                                                   column_selectable="single",
                                                                   selected_columns=[],
                                                                   selected_rows=[],
                                                                   page_action="native",
                                                                   page_current=0,
                                                                   page_size=10,
                                                                   style_as_list_view=True,
                                                                   style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                                                                   style_cell={
                                                                       'backgroundColor': 'rgb(50, 50, 50)',
                                                                       'color': 'white'
                                                                   }),
                                              html.Div(id='container-nasdaq-button')

                                          ]),
                                  dcc.Tab(label='CRYPTO CURRENCY',
                                          style=tab_style,
                                          selected_style=tab_selected_style,
                                          children=[
                                              html.Button('Upload new data',
                                                          id='upload-crypto-button',
                                                          title='Upload most recent crypto data',
                                                          n_clicks=0,
                                                          style={
                                                              'backgroundColor': 'rgb(50, 50, 50)',
                                                              'color': 'white'}),

                                              html.Button('Draw a graphic',
                                                          id='draw-crypto-button',
                                                          title='Draw most recent crypto data',
                                                          n_clicks=0,
                                                          style={
                                                              'backgroundColor': 'rgb(50, 50, 50)',
                                                              'color': 'white'}),

                                              dcc.Graph(id='crypto-graph',
                                                        figure=fig2),

                                              dash_table.DataTable(id='datatable-crypto-interactivity',
                                                                   columns=column_crypto_data,
                                                                   data=table_crypto_data,
                                                                   editable=True,
                                                                   filter_action="native",
                                                                   sort_action="native",
                                                                   sort_mode="multi",
                                                                   column_selectable="single",
                                                                   selected_columns=[],
                                                                   selected_rows=[],
                                                                   page_action="native",
                                                                   page_current=0,
                                                                   page_size=10,
                                                                   style_as_list_view=True,
                                                                   style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                                                                   style_cell={
                                                                       'backgroundColor': 'rgb(50, 50, 50)',
                                                                       'color': 'white'
                                                                   }),
                                              html.Div(id='container-crypto-button')

                                          ]),
                                  dcc.Tab(label='ECONOMICS',
                                          style=tab_style,
                                          selected_style=tab_selected_style,
                                          children=[
                                              dcc.Graph(id='sector-graph',
                                                        figure=fig3),

                                              dash_table.DataTable(id='datatable-sectors-interactivity',
                                                                   columns=([{'id': 'rank', 'name': 'rank'}] +
                                                                            [{"name": i, "id": i} for i
                                                                             in dict(SECTORS)]),
                                                                   data=[
                                                                       dict(rank=i,
                                                                            **{param: 0 for param in dict(SECTORS)})
                                                                       for i in rank_names],
                                                                   editable=True,
                                                                   filter_action="native",
                                                                   sort_action="native",
                                                                   sort_mode="multi",
                                                                   column_selectable="single",
                                                                   selected_columns=[],
                                                                   selected_rows=[],
                                                                   page_action="native",
                                                                   page_current=0,
                                                                   page_size=10,
                                                                   style_as_list_view=True,
                                                                   style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                                                                   style_cell={
                                                                       'backgroundColor': 'rgb(50, 50, 50)',
                                                                       'color': 'white'
                                                                   })

                                          ]),
                              ])
                          ])


drawer()


@app.callback(Output('container-nasdaq-button', 'children'),
              Input('upload-nasdaq-button', 'n_clicks'),
              Input('draw-nasdaq-button', 'n_clicks'))
def button_click_nasdaq(*args):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'upload-nasdaq-button' in changed_id:
        threads = []

        for index, company_name in enumerate(STOCKS.values()):
            thread = Thread(target=download_and_save_nasdaq_df, args=[company_name])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if 'draw-nasdaq-button' in changed_id:
        nasdaq_data, general_nasdaq_df = nasdaq_data_maker()
        return drawer(figure_nasdaq_data=nasdaq_data,
                      table_nasdaq_data=general_nasdaq_df.drop(columns='Unnamed: 0').to_dict('records'))


@app.callback(Output('container-crypto-button', 'children'),
              Input('upload-crypto-button', 'n_clicks'),
              Input('draw-crypto-button', 'n_clicks'))
def button_click_crypto(*args):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'upload-crypto-button' in changed_id:
        threads = []

        for index, crypto_name in enumerate(CRYPTOS.values()):
            thread = Thread(target=download_and_save_crypto_df, args=[crypto_name])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if 'draw-crypto-button' in changed_id:
        crypto_data, general_crypto_df = crypto_data_maker()
        return drawer(figure_crypto_data=crypto_data,
                      table_crypto_data=general_crypto_df.drop(columns='Unnamed: 0').to_dict('records'))


if __name__ == '__main__':
    app.run_server(debug=True)
