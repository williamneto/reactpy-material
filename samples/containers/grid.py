from reactpy import component, run, html
from reactpy_material import grid,button

@component
def app():
    return html.div(
        grid(
            grid(
                grid(
                    grid(
                        button("2 button"),
                        attrs={
                            "item": True,
                            "xs": 6
                        }
                    ),
                    grid(
                        button("3 button"),
                        attrs={
                            "item": True,
                            "xs": 6
                        }
                    ),
                    attrs={
                        "container": True
                    }
                ),
                attrs={
                    "item": True,
                    "xs": 6
                }
            ),
            grid(
                button("4 button"),
                attrs={
                    "item": True,
                    "xs": 6
                }
            ),
            attrs={
                "container": True
            }
        )
    )

run(app)