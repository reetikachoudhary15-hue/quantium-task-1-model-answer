# python_task3_sales_visualiser.py

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/daily_sales.csv")  # make sure this CSV exists
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    # Header
    html.H1("Pink Morsels Sales Visualiser"),

    # Region picker
    dcc.RadioItems(
        id="region-picker",  # this ID is used in tests
        options=[
            {"label": "North", "value": "North"},
            {"label": "South", "value": "South"},
            {"label": "East", "value": "East"},
            {"label": "West", "value": "West"}
        ],
        value="North"
    ),

    # Graph
    dcc.Graph(
        id="sales-graph"
    )
])

# Callback to update graph based on region
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):
    filtered_df = df[df["region"] == selected_region] if "region" in df.columns else df
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales for {selected_region}")
    return fig

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)
