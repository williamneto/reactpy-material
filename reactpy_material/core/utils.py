from reactpy.core.types import VdomChild
from reactpy.core.component import Component

def _parse_children(children: VdomChild):
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return children_items