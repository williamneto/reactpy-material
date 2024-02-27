
# reactpy-material

This project provide Material UI components to be used in [reactpy](github.com/reactive-python/reactpy) projects. 
For a deep understanding of the components and its properties check the [Material UI Docs](https://mui.com/material-ui/getting-started/).

## Available components

Layout
- [Box](https://mui.com/material-ui/react-box/)
- [Container](https://mui.com/material-ui/react-container/)
- [Form Contol](https://mui.com/material-ui/api/form-control/)
- [Grid](https://mui.com/material-ui/react-grid/)
- [Stack](https://mui.com/material-ui/react-stack/)

Inputs
- [Autocomplete](https://mui.com/material-ui/react-autocomplete/)
- [Button](https://mui.com/material-ui/react-button/)
- [Button group](https://mui.com/material-ui/react-button-group/)
- [Checkbox](https://mui.com/material-ui/react-checkbox/)
- [Chip](https://mui.com/material-ui/react-chip/)
- [Input](https://mui.com/material-ui/api/input/)
- [Input label](https://mui.com/material-ui/api/input-label/)
- [Select](https://mui.com/material-ui/react-select/)
- [Text field](https://mui.com/material-ui/react-text-field/)
- [Switch](https://mui.com/material-ui/react-switch/)

Data display
- [Icons](https://mui.com/material-ui/icons/)
- [Typography](https://mui.com/material-ui/react-typography/)
- [Table container](https://mui.com/material-ui/react-table/)
- [Table](https://mui.com/material-ui/react-table/)
- [Table body](https://mui.com/material-ui/react-table/)
- [Table head](https://mui.com/material-ui/react-table/)
- [Table row](https://mui.com/material-ui/react-table/)
- [Table cell](https://mui.com/material-ui/react-table/)

Navigation
- [Speed dial](https://mui.com/material-ui/react-speed-dial/)
- [Pagination](https://mui.com/material-ui/react-pagination/)
- [Menu](https://mui.com/material-ui/react-menu/)
- [Menu item](https://mui.com/material-ui/api/menu-item/)
- [Tabs](https://mui.com/material-ui/react-tabs/)

## Samples

#### Button
[*Reference*](https://mui.com/material-ui/react-button/)
```
from reactpy import component
from reactpy_material import button

@component
def app()
    return ( 
        button(
            "Hello world", 
            attrs={
                "variant": "contained", 
                "href": "#test"
            }
        )
    )
```

#### Typography
[Reference](https://mui.com/material-ui/react-typography/)
```
@component
def app():
    return html.div(
        typography(
            "h1. Heading",
            attrs={
                "variant": "h1"
            }
        )
    )

run(app)
```

Check the [samples/](https://github.com/williamneto/reactpy-material/tree/main/samples) folder to see more samples of the available components.