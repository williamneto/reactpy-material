from reactpy import component, html, run
from reactpy.core.hooks import use_state
from reactpy_material import button, autocomplete, checkbox, select

@component
def app():
    complete_options = [
        { "label": 'The Shawshank Redemption', "year": 1994 },
        { "label": 'The Godfather', "year": 1972 },
        { "label": 'The Godfather: Part II', "year": 1974 },
        { "label": 'The Dark Knight', "year": 2008 },
    ]

    select_options = [
        { "label": 'The Shawshank Redemption', "value": 1994 },
        { "label": 'The Godfather', "value": 1972 },
        { "label": 'The Godfather: Part II', "value": 1974 },
        { "label": 'The Dark Knight', "value": 2008 },
    ]
    def click(e):
        print(e)

    selected_val, set_selected_val = use_state("")
    selected_label, set_selected_label = use_state("")

    select_open, set_select_open = use_state(False)

    def handle_change(e):
        set_selected_val(e.target.value)
        print(selected_val)

    return html.div(
        button(
            "Hello world", 
            attrs={
                "variant": "contained", 
                "href": "#test"
            }
        ),
        autocomplete(
            {
                "options": complete_options,
                "label": "Movies",
                "sx": {"width": 300}
            }
        ),
        html.label(
            "Check",
            checkbox(
                attrs={
                    "onClick": lambda e: click(e),
                    "color": "success"
                }
            )
        ),
        select(
            attrs={
                "options": select_options,
                "label": "Movie",
                "open": select_open,
                "onChange": lambda e: print(e),
                "onOpen": lambda e: set_select_open(True),
                "onClose": lambda e: set_select_open(False),
                "value": selected_val,
                "style": {"width": "100%"}
            }
        )
    )

run(app)