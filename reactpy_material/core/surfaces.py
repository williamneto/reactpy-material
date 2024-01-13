from pathlib import Path
from typing import Any

from reactpy import component
from reactpy.core.component import Component
from reactpy.web.module import export, module_from_file
from reactpy.core.types import VdomChild

from .utils import _parse_children

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
    return md_accordion(attrs, _parse_children(children))

@component
def accordion_summary(*children: VdomChild, attrs: Any = {}):    
    return md_accordion_summary(attrs, _parse_children(children))

@component
def accordion_actions(*children: VdomChild, attrs: Any = {}):    
    return md_accordion_actions(attrs, _parse_children(children))

@component
def accordion_details(*children: VdomChild, attrs: Any = {}):    
    return md_accordion_details(attrs, _parse_children(children))