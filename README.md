
# reactpy-material

Material UI components for reactpy projects

## Components

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


#### Autocomplete
[*Reference*](https://mui.com/material-ui/react-autocomplete/)
```
from reactpy import component
from reactpy_material import autocomplete

@component
def app()
    options = [
        { "label": 'The Shawshank Redemption', "year": 1994 },
        { "label": 'The Godfather', "year": 1972 },
        { "label": 'The Godfather: Part II', "year": 1974 },
        { "label": 'The Dark Knight', "year": 2008 },
    ]
    return (
        autocomplete(
            {
                "options": options,
                "label": "Movies"
            }
        )
    )
```

#### Checkbox
[*Reference*](https://mui.com/material-ui/react-checkbox/)
```
from reactpy import component, html
from reactpy_material import checkbox

@component
def app()
    return (
        html.label(
            "Check",
            checkbox(
                attrs={
                    "color": "success"
                }
            )
        )
    )
```
