# Crop  

Crop.py details an example for creating a cropped pdf using the small format, the one with two horizontal lines thatd delineate
the column names. First the script converts a page of a pdf into a jpeg image, then using edge and line detection, we crop the
page twice using the detected line. Finally, we reduce the original pdf to its cropped equivalent. 


# Getting Starting 

1. Make sure to have `virtualenv` install globally with pip.
2. Create a virtual environmnet with  `virtualenv -p python3 env`
3. Activate the virtual environmengt with  `source env/bin/activate`
4. Install the dependencies with `pip install -r requirements.txt`
