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

md_icon = export(_js_module, "MDIcon")
md_typography = export(_js_module, "MDTypography")
md_table_row = export(_js_module, "MDTableRow")
md_table_head = export(_js_module, "MDTableHead")
md_table_cell = export(_js_module, "MDTableCell")
md_table_body = export(_js_module, "MDTableBody")
md_table = export(_js_module, "MDTable")
md_table_container = export(_js_module, "MDTableContainer")
md_datagrid = export(_js_module, "MDDataGrid")

@component
def icon(attrs: Any = {}):
    return md_icon(attrs)

@component
def typography(*children: VdomChild, attrs: Any = {}):
    return md_typography(attrs, _parse_children(children))

@component
def table_row(*children: VdomChild, attrs: Any = {}):
    return md_table_row(attrs, _parse_children(children))

@component
def table_head(*children: VdomChild, attrs: Any = {}):
    return md_table_head(attrs, _parse_children(children))

@component
def table_cell(*children: VdomChild, attrs: Any = {}):
    return md_table_cell(attrs, _parse_children(children))

@component
def table_body(*children: VdomChild, attrs: Any = {}):
    return md_table_body(attrs, _parse_children(children))

@component
def table(*children: VdomChild, attrs: Any = {}):
    return md_table(attrs, _parse_children(children))

@component
def table_container(*children: VdomChild, attrs: Any = {}):
    return md_table_container(attrs, _parse_children(children))


@component
def datagrid(attrs: Any = {}):
    return md_datagrid(attrs)
