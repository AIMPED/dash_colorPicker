from dash import html


def chunk(input_list, chunk_lengths):
    output_list = []
    for length in chunk_lengths:
        output_list.append(input_list[:length])
        input_list = input_list[length:]
    return output_list


def check_margin(i):
    if i == 0:
        return {'margin-top': '0.0%'}
    else:
        return {'margin-top': '-5.4%'}


def gen_swatches(colors: list) -> list:
    idx = 0
    content = []
    for row in colors:
        row_length = len(row)
        tmp = html.Div(
            [
                html.Div(
                    className='col d-flex justify-content-center',
                    children=[
                        html.Div(
                            id={'type': 'outer', 'index': idx + sub_idx},
                            className='hex3',
                            style={'background-color': 'black'},
                            children=html.Div(
                                id={'type': 'inner', 'index': idx + sub_idx},
                                className='hex3 inner',
                                style={'background-color': color}
                            )
                        )
                        for sub_idx, color in enumerate(row)
                    ]
                )
            ],
            style=check_margin(idx)
        )
        content.append(tmp)
        idx += row_length
    return content
