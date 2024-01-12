from reactpy import run, component, use_state
from reactpy_material import stack, pagination, typography

@component
def app():
    value, set_value = use_state(1)

    def page_change(event, value):
        set_value(value)

    return stack(
        typography("Page %s" % value),
        pagination(
            attrs={
                "count": 10,
                "page": value,
                "onChange": page_change
            }
        )
    )

run(app)