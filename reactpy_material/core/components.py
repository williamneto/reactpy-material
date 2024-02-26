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

md_button = export(_js_module, "MDButton")
md_button_group = export(_js_module, "MDButtonGroup")
md_autocomplete = export(_js_module, "MDAutoComplete")
md_checkbox = export(_js_module, "MDCheckbox")
md_select = export(_js_module, "MDSelect")
md_text_field = export(_js_module, "MDTextField")
md_switch = export(_js_module, "MDSwitch")
md_input = export(_js_module, "MDInput")
md_input_label = export(_js_module, "MDInputLabel")
md_menu_item = export(_js_module, "MDMenuItem")
md_chip = export(_js_module, "MDChip")

@component
def button(*children: VdomChild, attrs: Any = {}):
    return md_button(attrs, *children)

@component
def button_group(*children: VdomChild, attrs: Any = {}):
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_button_group(attrs, children_items)

@component
def autocomplete(attrs: Any = {}):
    return md_autocomplete(attrs)

@component
def checkbox(attrs: Any = {}):
    return md_checkbox(attrs)

@component
def select(*children: VdomChild, attrs: Any = {}):
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )
    return md_select(attrs, children_items)


@component
def text_field(attrs: Any = {}):
    return md_text_field(attrs)


@component
def switch(attrs: Any = {}):
    return md_switch(attrs)


@component
def input_label(*children: VdomChild, attrs: Any = {}):
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_input_label(attrs, children_items)


@component
def menu_item(*children: VdomChild, attrs: Any = {}):
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_menu_item(attrs, children_items)


@component
def chip(attrs: Any = {}):
    return md_chip(attrs)
