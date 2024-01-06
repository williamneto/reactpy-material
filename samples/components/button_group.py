from reactpy import component, run
from reactpy_material import button, button_group

@component
def app():
    return ( 
        button_group(
            button(
                "First button", 
                attrs={                     
                    "href": "#test"
                }
            ),
            button(
                "Second button", 
                attrs={                     
                    "href": "#test"
                }
            ),
            attrs={
                "variant": "contained"
            }
        )
    )

run(app)