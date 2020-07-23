# folder-scripting

### Automated scripting tool for placing the relevant PowerPoint & Word documents into the right folders
======

##### How it works
This simple program reads in a csv file of a certain format and allocates the right powerpoint slides associated to its respecting teacher. Using the pandas library, it will store all of its data onto a dataframe whilst removing unnecessary content or invalid data entries on the csv.

> NOTE: CSV must be placed in the project folder along with the code
> NOTE: directories for each PC will be different, please ensure it is changed at the begining in main.py

It will proceed in making a new folder directory (according to the date needed) in its *destination folder*. It will also make subfolders with the names of the teachers.

!(https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


It will then read through the source folder for all the PowerPoints and Word Documents, storing them onto a dictionary for efficiency.



