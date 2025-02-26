#TASK1
"""import os
path = "C:\\Users\kamshat" 
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))"""

#TASK2
import os
path = "C:\\Users" 
"""print("Exists", os.path.exists(path))
print("Chitabel\'nost':",os.access(path,os.R_OK))
print("Wrtiteability:",os.access(path,os.W_OK))
print("Executability:",os.access(path,os.X_OK))"""

#TASK3
"""path = "C:\\Users\kamshat" 
if os.path.exists(path):
    print("File name:",os.path.basename(path))
    print("Directory name:",os.path.dirname(path))
else:
    print("Path doesnt exist")"""

#TASK4
"""with open("C:\\Users\\kamshat\\Desktop\\PP2\\lab06\\file.txt") as file:
    lines= file.readlines()
    total_lines =len(lines)
    print("total is :",total_lines)"""

