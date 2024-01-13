from reactpy import component, run
import reactpy_material as rp_m

@component
def app():
    return rp_m.container(
        rp_m.circular_progress(
            attrs={
                "color": "inherit"
            }
        ),
        rp_m.linear_progress(
            attrs={
                "color": "inherit"
            }
        )
    )

run(app)