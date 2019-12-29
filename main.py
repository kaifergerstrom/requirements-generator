
import pip
import cv2
from difflib import get_close_matches

filename = "test_import.py"

def closeMatches(patterns, word): 
    print(get_close_matches(word, patterns))

def get_libraries(filename):
    keys = ['from', 'import', 'as']  # Keywords to determine import lines
    s_keys = [" import ", " as "]
    libraries = []  # Empty list to store final values
    with open(filename, "rb") as f:  # Open the python file
    
        for line in f:  # Loop through all the lines
            line = line.decode("utf-8").strip()  # Decode the line to utf-8
            first = line.partition(' ')[0]  # Find the first word (for keyword searching)

            if first in keys:  # Check if first word is in keywords
                line = line.split(first, 1)[1].strip()  # Cut the keyword from the line and isolate second half

                for key in s_keys:  # Check if any other secondary keywords are still in string
                    if key in line:  # If the key is in the line, remove it and return first half
                        line = line.split(key)[0]
                
                if "," in line:  # Check if comma is in line for one line import format
                    for l in line.split(","):  # For all the libraries in the list
                        libraries.append(l)  # Add them separately
                elif "." in line:  # Check if period in line
                    libraries.append(line.split(".")[0])  # Isolate first half of string
                else:
                    libraries.append(line)  # If passes all tests, append as is

    libraries = [s.strip() for s in libraries]  # Strip floating spaces off all strings in list
    return libraries  # Return the formatted list

libraries = get_libraries(filename)
installed = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])