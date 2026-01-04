# task3_sales_visualiser.py

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load and prepare data
df = pd.read_csv("data/daily_sales.csv")  # Make sure this path is correct
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = Dash(__name__)

# Layout with CSS styling
app.layout = html.Div(
    style={
        "font-family": "Arial, sans-serif",
        "background-color": "#fdf6f0",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "text-align": "center",
                "color": "#e75480",
                "margin-bottom": "40px",
                "font-size": "40px"
            }
        ),
        html.Div(
            children=[
                html.Label("Select Region:", style={"font-weight": "bold", "margin-right": "10px", "font-size": "18px"}),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"}
                    ],
                    value="all",
                    inline=True,
                    style={"margin-bottom": "30px", "font-size": "16px", "color": "#333333"}
                ),
            ],
            style={"text-align": "center"}
        ),
        dcc.Graph(
            id="sales-line-chart",
            style={
                "border": "2px solid #e75480",
                "padding": "10px",
                "border-radius": "10px",
                "background-color": "#ffffff"
            }
        )
    ]
)

# Callback to update chart based on region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title=f"Sales Over Time ({selected_region.capitalize()})",
        markers=True
    )

    # Styling for the figure
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#fdf6f0",
        title_font_size=24,
        xaxis_title="Date",
        yaxis_title="Sales",
        xaxis=dict(showgrid=True, gridcolor="#f0e5e5"),
        yaxis=dict(showgrid=True, gridcolor="#f0e5e5"),
        font=dict(color="#333333")
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
