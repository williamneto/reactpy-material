from reactpy import component, run, html, use_state
from reactpy_material import chip


@component
def app():

    color, set_color = use_state("success")

    def handle_click(event):
        print(event)
        if color == "success":
            set_color("error")
        else:
            set_color("success")

    return (
        html.div(
            chip(
                attrs={
                    "label": "Click me!",
                    "variant": "filled",
                    "style": {"margin": "5px"},
                    "color": color,
                    "clickable": True,
                    "on_click": handle_click
                }
            )
        )
    )

run(app)
