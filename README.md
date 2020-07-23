# folder-scripting

### Automated scripting tool for placing the relevant PowerPoint & Word documents into the right folders
------

##### How it works
This simple program reads in a csv file of a certain format and allocates the right powerpoint slides associated to its respecting teacher. Using the pandas library, it will store all of its data onto a dataframe whilst removing unnecessary content or invalid data entries on the csv.

> NOTE: CSV must be placed in the project folder along with the code

> NOTE: directories for each PC will be different, please ensure it is changed at the begining in main.py

It will proceed in making a new folder directory (according to the date needed) in its *destination folder*. It will also make subfolders with the names of the teachers.

![alt text](https://github.com/Shankskun/folder-scripting/blob/master/img/daily-folder.png "Daily folder")


![alt text](https://github.com/Shankskun/folder-scripting/blob/master/img/names.png "Names")

It will then read through the source folder for all the PowerPoints and Word Documents, storing them onto a dictionary for efficiency. After which it will read data stored in the Dataframe from the CSV provided earlier, where the data will be used to search for the directory of the actualy file stored. This allows it to copy the src files to its destination file. If the program fails to find a file from the dictionary, it will produce a TXT file indicating the files that it failed to find. Program will run until it reaches the end of the CSV.

------


##### Use case
This application is built to help assist the Operation team at AiEnglish, reducing their workload of relentless copying and pasting of PowerPoints; thus this is coded heavily to suite their needs. If you wish to use this code, go ahead but they will be a lot areas where you need to modify.


##### Credits
This code is written by Shaun Soong, Andrea Sha, Livy Xu, Will Mao
