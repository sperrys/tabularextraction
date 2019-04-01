# Structure Based Extraction

### Description 

This folder deals with the structural aspects. From the perspective of an OCR'd pdf of tabular data, this process 
concerns itself with deriving the structural layout of the page. It doesn't concern itself with the content of pdf at 
all, it should map the text on the pdf to columns and rows so that the content-based tool can go over it.  
  
In its current form, this is the most time-intensive portion and no strong 
solution for automating this process at a reasonable rate has been developed.

A memo explaining current state and complications lives [here.]([https://drive.google.com/open?id=1g1M_hvfWhJSZFraO7q1C6fQIy0mgGJY50Sl7K1pZlwY)

### Potential Avenues 

#### Excalibur

[Excalibur](https://github.com/camelot-dev/excalibur) is a web based program that nicely allows for a user to open a browser, upload a pdf and cleanly draw column
separators and a table area on to each page. Even though this manuel intervention is time-instensive, it does a good
of creating row separators (unless when the text is rotated)

Usage Notes:

* Use the `stream` option (for tables without grid lines) 
* Set `split_text` to True (to split text along column separators)
* Do small pages ranges at a time (uploading more than 25 tends to take a while)  
* Use the `agregate_csvs.py` script to combine multiple pages into one output csv.

#### Camelot 

[Camelot](https://github.com/socialcopsdev/camelot) is the python package that the Excalibur web interface uses under the hood. This means it can be nicely 
integrated with a custom python program, but unfortunately attempts to automate the process via this method was 
difficult per the memo above. 


#### Custom Tool based on Pixel value

There's always a chance that with enough effort and expertise, a homegrown tool operating at a lower, pixel level like
camelot, could provide better results f for the usecase than what camelot or [Tabula](https://tabula.technology/) produces, 
but these libraries also have more time, feedback, and contributors behind them.  


### Comments and Implementations

Any feedback on potential improvement / development of this process is helpful. 

