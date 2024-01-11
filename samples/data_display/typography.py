from reactpy import component, run, html
from reactpy_material import typography

@component
def app():
    return html.div(
        typography(
            "h1. Heading",
            attrs={
                "variant": "h1"
            }
        )
    )

run(app)