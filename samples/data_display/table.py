from reactpy import html, run, component
from reactpy_material import (
    table_container,
    table,
    table_head,
    table_row,
    table_cell,
    table_body
)

@component
def app():
    table_data = [
        {"username": "joe", "email": "joe@mail.com"},
        {"username": "doe", "email": "doe@gmail.com"}
    ]
    def render_table_body():
        return (
            table_body(
                table_row(
                    table_cell(item.get("username")),
                    table_cell(item.get("email"))
                ) for item in table_data
            )
        )
            
    return html.div(
        table_container(
            table(
                table_head(
                    table_row(
                        table_cell("username"),
                        table_cell("E-mail")
                    )
                ),
                render_table_body(),
                attrs={
                    "sx": {"minWidth": 650}
                }
            )
        )
    )

run(app)