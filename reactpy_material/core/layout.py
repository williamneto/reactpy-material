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

md_grid = export(_js_module, "MDGrid")
md_container = export(_js_module, "MDContainer")
md_box = export(_js_module, "MDBox")
md_stack = export(_js_module, "MDStack")

@component
def grid(*children: VdomChild, attrs: Any = {}):    
    return md_grid(attrs, _parse_children(children))

@component
def container(*children: VdomChild, attrs: Any = {}):
    return md_container(attrs, _parse_children(children))

@component
def box(*children: VdomChild, attrs: Any = {}):
    return md_box(attrs, _parse_children(children))

@component
def stack(*children: VdomChild, attrs: Any = {}):
    return md_stack(attrs, _parse_children(children))

