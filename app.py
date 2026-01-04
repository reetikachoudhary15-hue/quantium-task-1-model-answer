import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/pink_morsels_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales ($)"
    }
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Soul Foods – Pink Morsels Sales Analysis"),

    html.P(
        "This visualisation shows Pink Morsels sales over time. "
        "The price increased on 15 January 2021, making it easy to see "
        "whether sales were higher before or after the increase."
    ),

    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
