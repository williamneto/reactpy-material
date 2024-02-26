from reactpy import component, run, html
from reactpy_material import switch

@component
def app():
    return (
        html.div(
            switch(
                attrs={
                    "checked": True,
                    "color": "secondary"
                }
            ),
            switch(
                attrs={
                    "checked": False
                }
            )
        )
    )

run(app)