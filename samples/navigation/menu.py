from reactpy import run, component, use_state
from reactpy_material import button, menu, menu_item, container

@component
def app():
    anchor_el, set_anchor_el = use_state(None)

    def handle_click(event):
        set_anchor_el(event["currentTarget"])

    def handle_close(event):
        set_anchor_el(None)
    
    return container(
        button(
            "Dashboard",
            attrs={
                "onClick": handle_click,
                "id": "menu-btn",
                "aria-controls": "main-menu" if anchor_el else None,
                "aria-haspopup": "true",
                "aria-expanded": "true" if anchor_el else None
            }
        ),
        menu(
            menu_item(
                "Profile",
                attrs={
                    "onClick": handle_close
                }
            ),
            menu_item(
                "Account",
                attrs={
                    "onClick": handle_close
                }
            ),
            menu_item(
                "Logout",
                attrs={
                    "onClick": handle_close
                }
            ),
            attrs={
                "id": "main-menu",
                "anchorEl": anchor_el,
                "open": True if anchor_el else False,
                "onClose": handle_close,
                "aria-labelled-by": "menu-btn",
                "anchorOrigin": {
                    "vertical": "top",
                    "horizontal": "left"
                },
                "transformOrigin": {
                    "vertical": "top",
                    "horizontal": "left"
                }
            }
        )
    )

run(app)