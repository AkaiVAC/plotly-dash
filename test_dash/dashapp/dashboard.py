import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[dbc.themes.MATERIA],
    )
    dash_app.layout = dbc.Container(
        dbc.Row(
            dbc.Col(
                [
                    html.H4(
                        "Change the value in the text box to see callbacks in action!"
                    ),
                    html.Div(
                        [
                            dbc.Input(
                                id="my-input",
                                value="initial value",
                                type="text",
                                autoFocus=True,
                            ),
                        ]
                    ),
                    html.Br(),
                    dbc.Card(id="my-output", body=True),
                    dbc.ListGroup(
                        [
                            dbc.ListGroupItem(
                                dbc.NavLink("Home", href="/", external_link=True)
                            ),
                            dbc.ListGroupItem(
                                dbc.NavLink("About", href="/about", external_link=True)
                            ),
                            dbc.ListGroupItem(
                                dbc.NavLink(
                                    "Internal Link — Dash App 2", href="/dashapp2"
                                )
                            ),
                            dbc.ListGroupItem(
                                dbc.NavLink(
                                    "External Link — Dash App 2",
                                    href="/dashapp2",
                                    external_link=True,
                                )
                            ),
                        ],
                        className="mt-4",
                    ),
                ],
                className="mt-5",
            )
        )
    )

    @dash_app.callback(
        Output(component_id="my-output", component_property="children"),
        Input(component_id="my-input", component_property="value"),
    )
    def update_output_div(input_value):
        return f"Output: {input_value}"

    return dash_app.server
