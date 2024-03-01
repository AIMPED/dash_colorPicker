import dash
from dash import html, dcc, Input, Output, ALL, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import numpy as np
import utils

colors = ['#003366','#336699','#3366CC','#003399','#000099','#0000CC','#000066','#006666','#006699','#0099CC','#0066CC','#0033CC','#0000FF','#3333FF','#333399','#669999','#009999','#33CCCC','#00CCFF','#0099FF','#0066FF','#3366FF','#3333CC','#666699','#339966','#00CC99','#00FFCC','#00FFFF','#33CCFF','#3399FF','#6699FF','#6666FF','#6600FF','#6600CC','#339933','#00CC66','#00FF99','#66FFCC','#66FFFF','#66CCFF','#99CCFF','#9999FF','#9966FF','#9933FF','#9900FF','#006600','#00CC00','#00FF00','#66FF99','#99FFCC','#CCFFFF','#CCCCFF','#CC99FF','#CC66FF','#CC33FF','#CC00FF','#9900CC','#003300','#009933','#33CC33','#66FF66','#99FF99','#CCFFCC','#FFFFFF','#FFCCFF','#FF99FF','#FF66FF','#FF00FF','#CC00CC','#660066','#336600','#009900','#66FF33','#99FF66','#CCFF99','#FFFFCC','#FFCCCC','#FF99CC','#FF66CC','#FF33CC','#CC0099','#993399','#333300','#669900','#99FF33','#CCFF66','#FFFF99','#FFCC99','#FF9999','#FF6699','#FF3399','#CC3399','#990099','#666633','#99CC00','#CCFF33','#FFFF66','#FFCC66','#FF9966','#FF6666','#FF0066','#CC6699','#993366','#999966','#CCCC00','#FFFF00','#FFCC00','#FF9933','#FF6600','#FF5050','#CC0066','#660033','#996633','#CC9900','#FF9900','#CC6600','#FF3300','#FF0000','#CC0000','#990033','#663300','#996600','#CC3300','#993300','#990000','#800000','#993333']

# these are the predefined chunk lengths. This is basically the number of
# swatches per line. The first line and last line have 5 swatches
# the sum of all swatches has to correspond to the number of colors (61)
chunk_lengths = [7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7]

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


app.clientside_callback(
    """
    function(click_data, current_styles) {
        return dash_clientside.clientside.updateStyle(click_data, current_styles);
    }
    """,
    Output({'type': 'outer', 'index': ALL}, 'style'),
    [Input('graph', 'clickData')],
    [State({'type': 'outer', 'index': ALL}, 'style')]
)


if __name__ == "__main__":
    app.run(debug=True)
