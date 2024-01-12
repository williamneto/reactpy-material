from pathlib import Path
from typing import Any

from reactpy import component
from reactpy.core.component import Component
from reactpy.web.module import export, module_from_file
from reactpy.core.types import VdomChild

_js_module = module_from_file(
    "reactpy-material",
    file=Path(__file__).parents[1] / "bundle.js"
)

md_tab = export(_js_module, "MDTab")
md_tabs = export(_js_module, "MDTabs")
md_pagination = export(_js_module, "MDPagination")

@component
def tab(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_tab(attrs, children_items)

@component
def tabs(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_tabs(attrs, children_items)

@component
def pagination(attrs: Any = {}):
    return md_pagination(attrs)