from reactpy import run, component
from reactpy_material import grid, box

@component
def app():
    data = ["item 1", "item 2", "item 3"]

    return grid(
        [box(item) for item in data]
    )

run(app)