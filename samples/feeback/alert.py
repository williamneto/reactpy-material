from reactpy import component, run
import reactpy_material as rp_m

@component
def app():
    return rp_m.container(
        rp_m.alert(
            "Success alert",
            attrs={
                "severity": "success"
            }
        )
    )

run(app)