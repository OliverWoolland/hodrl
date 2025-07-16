from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

import hodrl.ui.layout as layout

app = Dash(
    external_stylesheets=[dbc.themes.LUX],
    suppress_callback_exceptions=True
)

app.layout = dmc.MantineProvider(
    children=dbc.Container([
        layout.get_main_accordion(),
    ], fluid=True),
)

def main():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    main()
