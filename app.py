# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go

from get_alphavantage_data import *
from dash.dependencies import Input, Output
from threading import Thread

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'My Sigma Project'


def data_maker():
    data = []

    general_df = None
    companies_df = get_companies_df()

    for company_df in companies_df:
        if general_df is None:
            general_df = company_df
        else:
            general_df.append(company_df)

        data.append(go.Scatter(x=company_df.timestamp,
                               y=company_df.volume,
                               hovertext=company_df,
                               name=company_df.name.loc[0],
                               showlegend=True))
    return data, general_df


def drawer(figure_data=None, table_data=None, column_data=None):
    colors = {
        'background': 'black',
        'text': 'white'}

    if column_data is None:
        column_data = [{'id': 'timestamp', 'name': 'timestamp'},
                       {'id': 'open', 'name': 'open'},
                       {'id': 'high', 'name': 'high'},
                       {'id': 'low', 'name': 'low'},
                       {'id': 'close', 'name': 'close'},
                       {'id': 'volume', 'name': 'volume'},
                       {'id': 'name', 'name': 'name'}]

    fig = go.Figure(data=figure_data)

    fig.update_layout(plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'],
                      font_color=colors['text'])

    app.layout = html.Div(style={'backgroundColor': colors['background']},
                          children=[
                              html.H1(children='NASDAQ INDEXES',
                                      style={
                                          'textAlign': 'center',
                                          'color': colors['text']}),

                              html.Button('Upload new data',
                                          id='upload-button',
                                          title='Upload most recent company data',
                                          n_clicks=0,
                                          style={
                                              'backgroundColor': 'rgb(50, 50, 50)',
                                              'color': 'white'}),

                              html.Button('Draw a graphic',
                                          id='draw-button',
                                          title='Draw most recent company data',
                                          n_clicks=0,
                                          style={
                                              'backgroundColor': 'rgb(50, 50, 50)',
                                              'color': 'white'}),

                              dcc.Graph(id='example-graph',
                                        figure=fig),

                              dash_table.DataTable(id='datatable-interactivity',
                                                   columns=column_data,
                                                   data=table_data,
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
                              html.Div(id='container-button')
                          ])


drawer()


@app.callback(Output('container-button', 'children'),
              Input('upload-button', 'n_clicks'),
              Input('draw-button', 'n_clicks'))
def button_click(*args):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'upload-button' in changed_id:
        threads = []

        for index, company_name in enumerate(STOCKS.values()):
            thread = Thread(target=download_and_save_company_df, args=[company_name])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if 'draw-button' in changed_id:
        data, general_df = data_maker()
        return drawer(figure_data=data,
                      table_data=general_df.drop(columns='Unnamed: 0').to_dict('records'))


if __name__ == '__main__':
    app.run_server(debug=True)
