import dash
from dash import html, dcc, Input, Output, ALL, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import numpy as np
import utils

colors = [
    '#FFFFFF',
    '#222A2A',
    '#FB0D0D',
    '#0D2A63',
    '#511CFB',
    '#EB663B',
    '#E15F99',
    '#FFC000',
    '#2E91E5',
    '#1CA71C',
    '#F2F2F2',
    '#808080',
    '#FFB9B9',
    '#D6DCE4',
    '#D9E1F2',
    '#FCE4D6',
    '#FFC5FB',
    '#FFF2CC',
    '#DDEBF7',
    '#E2EFDA',
    '#D9D9D9',
    '#595959',
    '#FD5F5F',
    '#ACB9CA',
    '#B4C6E7',
    '#F8CBAD',
    '#FF89FC',
    '#FFE699',
    '#BDD7EE',
    '#C6E0B4',
    '#BFBFBF',
    '#404040',
    '#F03838',
    '#8497B0',
    '#8EA9DB',
    '#F4B084',
    '#FE1EDE',
    '#FFD966',
    '#9BC2E6',
    '#A9D08E',
    '#A6A6A6',
    '#262626',
    '#E60000',
    '#333F4F',
    '#305496',
    '#C65911',
    '#CE04C0',
    '#BF8F00',
    '#2F75B5',
    '#548235',
    '#808080',
    '#0D0D0D',
    '#A20000',
    '#222B35',
    '#203764',
    '#833C0C',
    '#820479',
    '#806000',
    '#1F4E78',
    '#375623',
    'gray'
]

# these are the predefined chunk lengths. This is basically the number of
# swatches per line. The first line and last line have 5 swatches
# the sum of all swatches has to correspond to the number of colors (61)
chunk_lengths = [5, 6, 7, 8, 9, 8, 7, 6, 5]

# chunk the color list into the corresponding swatches per row
chunked_colors = utils.chunk(colors, chunk_lengths)

# create dummy figure
fig = go.Figure(layout=dict(width=1200, height=900))
for i, c in enumerate(colors, start=1):
    fig.add_scatter(
        x=np.arange(len(colors)),
        y=np.ones(len(colors))*i,
        mode='lines',
        name=c,
        line_color=c,
    )

app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    ]
)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    children=utils.gen_swatches(chunked_colors),
                    className='customContainer'
                ),
            ],
            className='col-4 d-flex justify-content-center'
        ),
        html.Div(
            dcc.Graph(id='graph', figure=fig),
            className='col-8 d-flex justify-content-center'
        )
    ],
    className='row min-vh-100'
)


@app.callback(
    Output({'type': 'outer', 'index': ALL}, 'style'),
    Input('graph', 'clickData'),
    State({'type': 'outer', 'index': ALL}, 'style'),
    prevent_initial_call=True
)
def do(click_data, current_styles):
    if not click_data:
        raise PreventUpdate

    # which curve has been clicked?
    clicked = click_data['points'][0]['curveNumber']

    # change style at corresponding index
    for counter, _ in enumerate(current_styles):
        if counter == clicked:
            current_styles[counter].update({'background-color': 'red'})
        else:
            current_styles[counter].update({'background-color': 'black'})
    return current_styles


if __name__ == "__main__":
    app.run(debug=True)
