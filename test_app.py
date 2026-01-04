# test_app.py

import pytest
from dash.testing.application_runners import import_app

# Fixture to import Dash app
@pytest.fixture
def dash_app():
    app = import_app("python_task3_sales_visualiser")  # match your app filename
    return app

# Test 1: Check header exists
def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Sales Visualiser" in header.text

# Test 2: Check graph exists
def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("div.js-plotly-plot")  # Dash Graph uses this class
    assert graph is not None

# Test 3: Check region picker exists
def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_picker = dash_duo.find_element("div#region-picker")  # matches the ID in layout
    assert region_picker is not None




