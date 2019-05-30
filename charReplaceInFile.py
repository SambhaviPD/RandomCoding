# Iterate through all files in a folder and replace 1st character
# from 0 to 1 and save the file. 
# As long as input files are small, this approach is pretty good

import os
from pathlib import Path

# Stores the path of the file charReplaceInFile.py
base_dir = os.path.dirname(os.path.abspath(__file__))
# labels is a folder that is present at the same level of charReplaceInFile.py
labels_dir = Path('labels')
# Iterate through all txt files in labels folder
for label in Path(base_dir / labels_dir).glob("**/*.txt"):
    print('File name: ', label)
    # Read in the label file
    with open(label, 'r') as file :
      labeldata = file.read()
    
    # Replace the target string, from 0 to 1, third parameter 1 means that
    # it stops with first occurence of search string
    labeldata = labeldata.replace('0', '1', 1)
    
    # Write new labeldata to file
    with open(label, 'w') as file:
      file.write(labeldata)
