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

md_button = export(_js_module, "MDButton")
md_button_group = export(_js_module, "MDButtonGroup")
md_autocomplete = export(_js_module, "MDAutoComplete")
md_checkbox = export(_js_module, "MDCheckbox")
md_select = export(_js_module, "MDSelect")
md_text_field = export(_js_module, "MDTextField")

@component
def button(*children: VdomChild, attrs: Any = {}):
    return md_button(attrs, *children)

@component
def button_group(*children: VdomChild, attrs: Any = {}):
    return md_button_group(attrs, _parse_children(children))

@component
def autocomplete(attrs: Any = {}):
    return md_autocomplete(attrs)

@component
def checkbox(attrs: Any = {}):
    return md_checkbox(attrs)

@component
def select(attrs: Any = {}):
    return md_select(attrs)

@component
def text_field(attrs: Any = {}):
    return md_text_field(attrs)