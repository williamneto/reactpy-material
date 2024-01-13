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

md_accordion = export(_js_module, "MDAccordion")
md_accordion_summary = export(_js_module, "MDAccordionSummary")
md_accordion_actions = export(_js_module, "MDAccordionActions")
md_accordion_details = export(_js_module, "MDAccordionDetails")

@component
def accordion(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_accordion(attrs, children_items)

@component
def accordion_summary(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_accordion_summary(attrs, children_items)

@component
def accordion_actions(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_accordion_actions(attrs, children_items)

@component
def accordion_details(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_accordion_details(attrs, children_items)