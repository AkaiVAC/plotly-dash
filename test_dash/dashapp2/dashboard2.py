import dash
import dash_bootstrap_components as dbc


def init_dashboard_2(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp2/",
        external_stylesheets=[dbc.themes.MATERIA],
    )
    dash_app.layout = dbc.Container(
        dbc.Row(
            dbc.Col(
                dbc.Alert("This is another app", color="success"),
                className="mt-5",
            )
        )
    )

    return dash_app.server
