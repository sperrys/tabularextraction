# Content Based Extraction

## Description

This tool is geared at properly extracting and validating content from OCR pdfs. This tool will likely not work well if the input csv
is not structurally deterministic, meaning a fixed mapping of input fields to relative positions of csv cells. This is specified in `config.INPUT_FIELD_STRUCTURAL_MAPPINGS`.
 
Rather, This tool is meant to be a way to validate and correct OCR text to an acceptable final csv form based on the fields specified in
 `config.CSV_OUTPUT_FIELDS` 

A memo explaining current state and rational lives [here.]([https://drive.google.com/open?id=1g1M_hvfWhJSZFraO7q1C6fQIy0mgGJY50Sl7K1pZlwY)


### Abstractions

Each abstraction has a particular role in the content extractor tool. Each abstraction gets its own folder with a 
README.md that describes its role and provides the implementation and interface.


* Db

* Parser 

* Validator

* Viewer

* Record


### Getting Started

1. Create a virtual environment with `virtualenv` it can be installed here.
2. Once installed globally, create a new virtual environment with python3 with `virtualenv -p python3 env`
3. Activate the virtualenv with `source env/bin/activate`
4. Install requirements within the virtual enviroment with `pip install -r requirements.txt`
5. Run with `python main.py` with the options specified in `config.py`