# Validators

## Description

In the content-based extraction, phase, validators represent the approval of a given value 
for a given output field. 

If the value passes all the logic in a validator, it's considered to be valid output for that ``field`.


## What's There 

Validators for each current output field, which mainly call generic number and string validators 
with different parameters


### Extending

Knowing the role of validators pre-existing validators can be easily edited in `validators.py` to add more use cases or 
stricter logic. 

If, for whatever reason a new validator is needed, the steps for properly integrating one are:

1. Write a validator function that takes a `value` and a `field` and returns either success or an error messages
   of the same format.
   
2. Name that validator function the output `field` its supposed to validate