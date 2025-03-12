#Write a Python program to list only directories, files and all directories, files in a specified path.
# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
# Write a Python program to count the number of lines in a text file.
# Write a Python program to write a list to a file.
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# Write a Python program to copy the contents of a file to another file
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

# TASK1
import os
path = "C:\\Users\kamshat" 
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))

#TASK2
import os
path = "C:\\Users" 
print("Exists", os.path.exists(path))
print("Chitabel\'nost':",os.access(path,os.R_OK))
print("Wrtiteability:",os.access(path,os.W_OK))
print("Executability:",os.access(path,os.X_OK))

#TASK3
path = "C:\\Users\kamshat" 
if os.path.exists(path):
    print("File name:",os.path.basename(path))
    print("Directory name:",os.path.dirname(path))
else:
    print("Path doesnt exist")

#TASK4
with open("C:\\Users\\kamshat\\Desktop\\PP2\\lab06\\file.txt") as file:
    lines= file.readlines()
    total_lines =len(lines)
    print("total is :",total_lines)

#TASK 5
def list_to_file(filename, data_list):
    with open(filename, "w") as file:
        for item in data_list:
            file.write(str(item) + "\n")
data = ["Hello", "world", "PP2"]
list_to_file("exapmle.txt", data)

#TASK 6
"""import string
for letter in string.ascii_uppercase:  # A to Z
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt\n")"""

#TASK 7
import os
def copy_file(source, destination):
    try:
        with open(source, "r") as src:
            content = src.read()
        with open(destination, "w") as dest:
            dest.write(content)
        print(f"Successfully copied {source} to {destination}")
    except FileNotFoundError:
        print(f"Error: {source} does not exist.")
    except IOError as e:
        print(f"Error copying file: {e}")
copy_file("source.txt", "destination.txt")

#TASK 8
import os

def delete_file(filepath):
    if os.path.exists(filepath):
        if os.access(filepath, os.W_OK):  
            os.remove(filepath)
            print(f"File '{filepath}' has been deleted.")
        else:
            print(f"Permission denied: Cannot delete '{filepath}'.")
    else:
        print(f"File '{filepath}' does not exist.")
delete_file("test.txt")

