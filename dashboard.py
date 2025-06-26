import pandas as pd
import numpy as np
from datetime import datetime
import dash
from dash import html, dcc
import plotly.express as px

# Simulated structured data (as if loaded from Postgres)
products = pd.DataFrame({
    "product": ["A", "B", "C"],
    "quantity": [100, 150, 200]
})

# Simulated time series data (as if loaded from InfluxDB)
now = datetime.now()
periods = 50
index = pd.date_range(end=now, periods=periods, freq="H")
timeseries = pd.DataFrame({
    "timestamp": index,
    "value": np.random.randn(periods).cumsum()
})

operation_fig = px.bar(products, x="product", y="quantity", title="运营报表")
process_fig = px.line(timeseries, x="timestamp", y="value", title="工艺管理")
device_fig = px.scatter(timeseries, x="timestamp", y="value", title="设备管理")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Nav([
        html.Ul([
            html.Li(html.A("运营报表", href="#op")),
            html.Li(html.A("工艺管理", href="#process")),
            html.Li(html.A("设备管理", href="#device")),
            html.Hr(),
            html.Li(html.A("数据连接", href="#data")),
        ], style={"listStyle": "none", "padding": 0}),
        html.Div("v1.0 © 2025 宁波华翔", style={"marginTop": "20px", "fontSize": "0.8em"}),
    ], style={"width": "200px", "float": "left", "padding": "10px", "borderRight": "1px solid #ccc"}),
    html.Div([
        html.Section([
            dcc.Graph(figure=operation_fig)
        ], id="op"),
        html.Section([
            dcc.Graph(figure=process_fig)
        ], id="process"),
        html.Section([
            dcc.Graph(figure=device_fig)
        ], id="device"),
    ], style={"marginLeft": "220px", "padding": "10px"})
])

if __name__ == "__main__":
    app.run(debug=True)
