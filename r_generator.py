
import subprocess, sys, os

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
    libraries = list(set(libraries))
    return libraries  # Return the formatted list


def create_requirements(libraries, output_path):
    with open("{}/requirements.txt".format(output_path), "w+") as f:
        for library in libraries:
            try:
                result = subprocess.check_output(['pip3', 'show', library]).decode('utf-8')
                version = result.split('\n')[1].split('Version:')[1].strip()
                f.write("{}=={}\n".format(library, version))
            except:
                pass


if __name__ == "__main__":
    file_path = sys.argv[1]
    path = os.path.split(file_path)[0]
    libraries = get_libraries(file_path)
    create_requirements(libraries, path)
