from reactpy import component, run, html
from reactpy_material import icon

@component
def app():
    return html.div(
        icon(
            {
                "icon": "AccessAlarmOutlined"
            }
        )
    )

run(app)