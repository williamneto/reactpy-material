from reactpy import component, run, html, use_state
from reactpy_material import form_control, input_label, select, box, typography, menu_item


@component
def app():
    value_selected, set_value_selected = use_state("one")

    def handle_change(value):
        set_value_selected(value)

    return html.div(
        box(
            form_control(
                input_label(
                    "My Input:",
                    attrs={"htmlFor": "my-input"},
                ),
                select(
                    menu_item("One", attrs={"value": "one"}),
                    menu_item("Two", attrs={"value": "two"}),
                    menu_item("Three", attrs={"value": "three"}),
                    attrs={
                        "value": value_selected,
                        "id": "my-input",
                        "onChange": lambda _, event: handle_change(event['props']['value'])
                    }),
            ),
            typography(f"Option selected: {value_selected}")
        )
    )


run(app)
