import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/updated_merged_data.csv')

# Initialize the Dash app with Bootstrap theme and custom CSS
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/assets/custom_styles.css'])
server = app.server  # Expose the server for deployment

# Function to create choropleth figures
def create_choropleth(data, column, title, colorscale, zmid=None):
    fig = px.choropleth(
        data,
        locations="Country",
        locationmode="country names",
        color=column,
        hover_name="Country",
        title=title,
        color_continuous_scale=colorscale,
        color_continuous_midpoint=zmid
    )
    fig.update_layout(
        title=dict(x=0.5),
        geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
        coloraxis_colorbar=dict(title=column.replace('_', ' '))
    )
    return fig

# Create figures for each map
fig1 = create_choropleth(
    df,
    "Diff_Traditional_vs_Secular",
    "Difference in Traditional vs Secular Values (ChatGPT - Survey)",
    px.colors.diverging.RdBu,
    zmid=0
)

fig2 = create_choropleth(
    df,
    "Abs_Diff_Traditional_vs_Secular",
    "Absolute Difference in Traditional vs Secular Values (ChatGPT - Survey)",
    px.colors.sequential.YlGnBu
)

fig3 = create_choropleth(
    df,
    "Diff_Survival_vs_SelfExpression",
    "Difference in Survival vs Self-Expression Values (ChatGPT - Survey)",
    px.colors.diverging.RdBu,
    zmid=0
)

fig4 = create_choropleth(
    df,
    "Abs_Diff_Survival_vs_SelfExpression",
    "Absolute Difference in Survival vs Self-Expression Values (ChatGPT - Survey)",
    px.colors.sequential.YlGnBu
)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Cultural Values Comparison: Survey vs ChatGPT",
                    className="text-center my-4"
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Description", className="card-title"),
                            html.P(
                                "This dashboard presents a comparative analysis of cultural values derived from two sources: "
                                "original survey data by Haerpfer et al. (2022) and ChatGPT's responses simulating an average individual in each country/region. "
                                "The maps illustrate differences and absolute differences in traditional vs. secular values and survival vs. self-expression values."
                            ),
                            html.P(
                                "Data covers 107 countries/territories categorized into 8 regions as per Inglehart R. (2005). "
                                "Values are normalized z-scores. Users can navigate through the tabs to view different comparative maps."
                            )
                        ]
                    ),
                    className="mb-4"
                )
            )
        ),
        dbc.Tabs(
            [
                dbc.Tab(dcc.Graph(figure=fig1, config={'displayModeBar': False}), label="Traditional vs Secular Difference"),
                dbc.Tab(dcc.Graph(figure=fig2, config={'displayModeBar': False}), label="Traditional vs Secular Absolute Difference"),
                dbc.Tab(dcc.Graph(figure=fig3, config={'displayModeBar': False}), label="Survival vs Self-Expression Difference"),
                dbc.Tab(dcc.Graph(figure=fig4, config={'displayModeBar': False}), label="Survival vs Self-Expression Absolute Difference"),
            ]
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("References", className="card-title"),
                            html.Ul(
                                [
                                    html.Li(
                                        "Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano J., "
                                        "Lagos, M., Norris, P., Ponarin, E., & Puranen, B. (eds.). (2022). World Values Survey: Round Seven - "
                                        "Country-Pooled Datafile Version 5.0. Madrid, Spain & Vienna, Austria: JD Systems Institute & WVSA Secretariat. "
                                        "DOI: 10.14281/18241.24"
                                    ),
                                    html.Li(
                                        "Inglehart, R., & Welzel, C. (2005). Modernization, cultural change, and democracy: The human development sequence. "
                                        "Cambridge University Press."
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        )
    ],
    fluid=True
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
