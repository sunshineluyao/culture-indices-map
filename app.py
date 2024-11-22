import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/updated_merged_data.csv')

# Initialize the Dash app
app = Dash(__name__)
server = app.server  # Expose the server for deployment

# Create the choropleth figure
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Diff_Traditional_vs_Secular",
    hover_name="Country",
    title="Difference in Traditional vs Secular Values (ChatGPT - Survey)",
    color_continuous_scale=px.colors.diverging.RdBu,
    color_continuous_midpoint=0  # Center the color scale around 0
)

fig.update_layout(
    title=dict(x=0.5),  # Center the title
    geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
    coloraxis_colorbar=dict(title="Difference (Centered at 0)")
)

# Define the layout
app.layout = html.Div(
    id="main-container",
    style={
        'background-color': '#2d00f7',  # Background color of the app
        'color': '#ffffff',
        'padding': '30px',
        'min-height': '100vh',
    },
    children=[
        # Title Section
        html.H1(
            "Difference in Traditional vs Secular Values (ChatGPT - Survey)",
            style={
                'text-align': 'center',
                'font-family': 'Arial, sans-serif',
                'margin-bottom': '20px',
                'padding': '10px',
                'border-radius': '10px',
                'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.5)',  # Shadow for 3D effect
                'background-color': '#2d00f7',  # Title background color
                'color': '#ffffff',  # White text for title
            }
        ),

        # Description Section
        html.Div(
            children=[
                html.P(
                    "This dashboard visualizes the difference between traditional and secular values derived from two sources:",
                    style={'font-size': '16px', 'font-weight': 'bold'}
                ),
                html.Ul([
                    html.Li("Original survey data by Haerpfer et al. (2022)."),
                    html.Li("ChatGPT's responses simulating an average individual in a country/region.")
                ]),
                html.P(
                    "Key details about the figure:",
                    style={'font-size': '16px', 'font-weight': 'bold'}
                ),
                html.Ul([
                    html.Li("Data covers 107 countries/territories across 8 regions as defined by Inglehart R. (2005)."),
                    html.Li("Color scale represents the difference between ChatGPT and survey values."),
                    html.Li("Values are normalized z-scores."),
                    html.Li("Users can hover over countries to see specific data.")
                ])
            ],
            style={
                'margin': '20px auto',
                'max-width': '900px',
                'background-color': '#ffffff',  # Description background color
                'padding': '20px',
                'border-radius': '10px',
                'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                'font-family': 'Arial, sans-serif',
                'color': '#2d00f7',  # Text color
            }
        ),

        # Graph Section
        html.Div(
            dcc.Graph(figure=fig),
            style={
                'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.5)',  # Shadow for 3D effect
                'border-radius': '10px',
            }
        ),

        # References Section
        html.Div(
            children=[
                html.H3("References", style={'text-align': 'left', 'font-weight': 'bold'}),
                html.Ul([
                    html.Li(
                        "Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano J., "
                        "M. Lagos, P. Norris, E. Ponarin & B. Puranen (eds.). 2022. World Values Survey: Round Seven - "
                        "Country-Pooled Datafile Version 5.0. Madrid, Spain & Vienna, Austria: JD Systems Institute & WVSA "
                        "Secretariat. DOI: 10.14281/18241.24"
                    ),
                    html.Li(
                        "Inglehart R., Welzel C. (2005). Modernization, cultural change, and democracy: the human development "
                        "sequence. Vol. 333. Cambridge University Press."
                    )
                ])
            ],
            style={
                'margin-top': '20px',
                'padding': '10px',
                'background-color': '#2d00f7',  # References background color
                'border-radius': '10px',
                'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                'font-family': 'Arial, sans-serif',
                'color': '#ffffff',  # White text
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
