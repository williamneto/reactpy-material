from pathlib import Path
from typing import Any

from reactpy import component
from reactpy.web.module import export, module_from_file
from reactpy.core.types import VdomChild

@component
def button(*children: VdomChild, attrs: Any = {}):
    return md_button(attrs, *children)

@component
def button_group(*children: VdomChild, attrs: Any = {}):
    return md_button_group(attrs, *children)

@component
def autocomplete(attrs: Any = {}):
    return md_autocomplete(attrs)

@component
def checkbox(attrs: Any = {}):
    return md_checkbox(attrs)

@component
def select(attrs: Any = {}):
    return md_select(attrs)

md_button, md_button_group, md_autocomplete, md_checkbox, md_select = export(
    module_from_file("reactpy-material", file=Path(__file__).parent / "bundle.js"),
    ("MDButton", "MDButtonGroup", "MDAutoComplete", "MDCheckbox", "MDSelect")
)