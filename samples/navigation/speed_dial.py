from reactpy import run, component
from reactpy_material import box, speed_dial, speed_dial_action, icon

@component
def app():
    return box(
        speed_dial(
            speed_dial_action(
                attrs={
                    "key": "share",
                    #"icon": icon({"Share"})
                }
            ),
            attrs={
                #"icon": icon({"icon": "Save"}),
                "sx": {
                    "position": "absolute",
                    "bottom": 10,
                    "right": 16
                }
            }
        ),
        attrs={
            "height": 320,
            "transform": "translateZ(0px)",
            "flexGrow": 1
        }
    )

run(app)