# Viewer

## Description 

The viewer abstraction is used to simulate navigation of the data. This means keep track of what page is currently 
being processed, along with what current structural cell is being examined.

Under the hood it works by loading logical pages as pandas dataframes, keyed by their page number. 


## TODO  

* Abstract out intervention interface from the viewer module. Right now the viewer module also handles user
  intervention data, but to clean things up it should be abstracted out.
  
* Create unit tests