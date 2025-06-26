# testCodex

This repository contains a simple Dash application (`dashboard.py`) that
shows how to build a dashboard using structured data (simulated Postgres)
and time-series data (simulated InfluxDB). The dashboard features
navigation items for **运营报表**, **工艺管理**, **设备管理**, and **数据连接**.

## Running

Install dependencies and start the server:

```bash
pip install dash pandas numpy plotly
python dashboard.py
```

The application displays basic charts and serves as a template for
further development.
