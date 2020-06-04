import os
import csv
import pandas as pd
from datetime import date

### Functions
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Unable to create Directory ->' + directory)


