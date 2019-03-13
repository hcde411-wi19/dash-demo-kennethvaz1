import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Excercise 2: For this excercise I wanted to explore if there was a correlation
# between horsepower(HP) and engine size for various luxury cars.

# no static data here

# initialize Dash environment and static folder
app = dash.Dash(__name__, static_folder='static')

# Using the data_car_2004.csv data set as my data frame
df = pd.read_csv('static/data_car_2004.csv')

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Engine Size vs Horsepower Scatter Plot'),

    # a div to put a short description
    html.Div(children='''
        This scatter plot shows a positive correlation between the engine size and horsepower of cars.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # Here we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x = df['HP'],
                    y = df['Engine Size (l)'],

                    # Creating circles as markers
                    mode = 'markers',

                    # Including the car name for people to look at when they hover
                    # any markers on my scatter plot
                    text = df['Vehicle Name'],
                    marker={
                        'size': 10,
                        'opacity': 0.8  # Set opacity to be a bit transparent, alleviating occlusion issues
                    }
                )
            ],

            'layout': {
                # Setting title, and labeling axes
                'title': 'Engine Size vs Horsepower for Various Model Cars',

                'xaxis': {'title': 'Horsepower'},
                'yaxis': {'title': 'Engine Size'},
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)