from reactpy import run, component, use_state, use_effect
from reactpy_material import container, tab, tabs, box

@component
def app():
    value, set_value = use_state("first")

    def handle_tab_change(event, value):
        set_value(value)

    return container(
        tabs(
            tab(
                attrs={"label": "First item", "value": "first"}
            ),
            tab(
                attrs={"label": "Second item", "value": "second"}
            ),
            attrs={
                "value": value,
                "onChange": handle_tab_change
            }
        ),
        container(
            box(
                value
            )
        ),
    )

run(app)