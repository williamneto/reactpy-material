from reactpy import html, run, component
from reactpy_material import datagrid


@component
def app():
    rows = [
        {'id': 1, 'col1': 'Hello', 'col2': 'World'},
        {'id': 2, 'col1': 'DataGrid', 'col2': 'is Awesome'},
        {'id': 3, 'col1': 'MUI', 'col2': 'is Amazing'}
    ]
    columns = [
        {'field': 'col1', 'headerName': 'Column 1', 'width': 150},
        {'field': 'col2', 'headerName': 'Column 2', 'width': 150}
    ]
    return html.div(
        datagrid(
            attrs={
                'rows': rows,
                'columns': columns
            }
        )
    )


run(app)
