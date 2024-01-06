import Button from "@mui/material/Button";
import ButtonGroup from '@mui/material/ButtonGroup';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Checkbox from '@mui/material/Checkbox';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';

import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';

import React from "react";
import ReactDOM from "react-dom";

export function bind(node) {
  return {
    create: (type, props, children) =>
      React.createElement(type, props, ...children),
    render: (element) => {
      ReactDOM.render(element, node);
    },
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  };
}

export function MDButton({ children, ...attrs }) {
  return (<Button {...attrs}>{children}</Button>);
}

export function MDButtonGroup({ children, ...attrs}) {
  return (
    <ButtonGroup {...attrs}>{children}</ButtonGroup>
  );
}

export function MDAutoComplete(attrs) {
  return (
    <Autocomplete 
      {...attrs} 
      renderInput={(params) => <TextField {...params} label={attrs.label} />}
    />
  );
}

export function MDCheckbox(attrs) {
  return <Checkbox {...attrs} />;
}

export function MDSelect(attrs) {
  return (
    <Select {...attrs}>
      {attrs.options.map( (item, key) => {
        return <MenuItem key={key} value={item.value}>{item.value}</MenuItem>
      })}
    </Select>
  );
}

export function MDGrid({ children, ...attrs}) {
  return (
    <Grid {...attrs}>
      {children}
    </Grid>
  );
}

export function MDContainer({ children, ...attrs}) {
  return (
    <Container {...attrs}>
      {children}
    </Container>
  );
}

export function MDBox({ children, ...attrs}) {
  return (
    <Box {...attrs}>
      {children}
    </Box>
  );
}