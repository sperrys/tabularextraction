# Parsers 


## Description

In the content-based extraction and validation phase, parsers represent any complex mapping between 
input fields and output fields. If structural extraction results in an input field x, if x by itself is not a 
desired output field, a **parser** should be invoked. 

The parser will break down a given input field 
based on a desired output field, returning just that embdedded output field. 

In this sense, not every input field needs a **parser**, just the input fields that encompass
several output fields. 



## What's There 

Currently, there are only 2 input fields that require parsers, but depending on the pdf and subsequent output of 
the structural extraction, more can be added without much effort.

### Current Parsers

**city_state_zip(value, field)** 

Provided a `value` that represents a city_state_zip input field, and an output `field` that the input field maps to, 
`'city', 'state', 'zip'`, parse that output field and return it, otherwise return an error.


**student_name(value, field)**

Provided a `value` that represents a city_state_zip input field, and an output `field` that the input field maps to, 
`'student_mi', 'student_first', 'student_last'`, parse that output field and return it, otherwise return an error.


### Extending

Knowing the role of parsers, pre-existing parsers can be easily edited in `parsers.py` to add more use case or 
better logic. 

If, for whatever reason a new parser is needed, the steps for properly integrating one are:

1. Write a parser function that takes a `value` and a `field` and returns error messages in the same existing 
   format and provides the parsing logic.
   
2. Make sure to call the parser function the name of the input field that you are trying to parse

3. In config.py, add an appropriate mapping between the input field and it's output field components.