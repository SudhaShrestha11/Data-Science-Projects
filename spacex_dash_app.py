# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                html.Div(dcc.Dropdown(id='site-dropdown',
                                    options=[{'label':'All Sites', 'value':'5'},
                                        {'label':'CCAFS LC-40', 'value':'1'},
                                        {'label':'VAFB SLC-4E', 'value':'2'},
                                        {'label':'KSC LC-39A', 'value':'3'},
                                        {'label':'CCAFS SLC-40', 'value':'4'}],
                                    value = 5,
                                    placeholder = 'Select a Lauch Site here'
                                    searchable=True)),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                #html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                # dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
                Input(component_id='site-dropdown', component_property = 'value'))

def get_graph(value):
    if value != 5:
       df= spacex_df[spacex_df['Launch Site']==value]
       fig = px.pie(df, names='class', title='Total Success Launches for site {}'.format(value))
       return fig
    else:
        allfig = px.pie(spacex_df, names='Launch Site', values = 'class', title='Total Success by Site')
        return allfig

# TASK 3: Add a slider to select payload range
dcc.RangeSlider(id='payload-slider',
                min=0,
                max=10000,
                step =1000,
                value = [min_payload,max_payload]
                )

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs,
# `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
    Input(component_id="payload-slider", component_property="value")]
    )

def update_graph(value):
    if value !=5:
        df_sp=spacex_df[spacex_df['Launch Site']==value]
        fig_sp=px.scatter(df_sp, x='Payload Mass (kg)', y='class', color='Booster Version Category')
        return fig_sp
    else:
        allfig_sp= px.scatter(spacex_df, x='Payload Mass (kg)', y='class', color='Booster Version Category')
        return allfig_sp

# Run the app
if __name__ == '__main__':
    app.run_server()
