import re
#TASK1
def match_str(s):
    pattern = r'^ab*$'
    return re.search(pattern,s)
test=["bac","ab","abb"]
for x in test:
    print(match_str(x))



#TASK2
def matching(s):
    pattern = r'^ab{2,3}$'
    return re.search(pattern,s)  
test=["bac","ab","abb","abbb"]
for x in test:
    print(matching(x))


#TASK 3
def Match(s):
    pattern = r'[a-z]+_[a-z]'
    return re.search(pattern,s)
test=["bac","ab","ab_ba","a_b"]
for x in test:
    print(Match(x))


#TASK 4
def m(s):
    pattern =r'[A-Z][a-z]+'
    return re.search(pattern,s)
       
test=["Az","az","aZ","Azzzz"]
for x in test:
    print(m(x))


#TASK 5
def m(s):
    pattern =r'^a\wb$'
    return re.search(pattern,s)
       
test=["bac","a1b","ab_ba","a_b"]
for x in test:
    print(m(x))


#TASK 6

import re
txt = "The rain. in ,Spain ;"
x = re.sub(r"[ .,]", ":", txt)
print(x)


#TASK 7
def replace_match(match):
    return match.group(1).upper()
def snake_to_camel(snake_str):
    return re.sub(r'_([a-zA-Z])', replace_match, snake_str)
snake_string = "this_is_an_example_text"
camel_string = snake_to_camel(snake_string)
print(camel_string)


#TASK 8
import re
text = "stringStr"
pattern = r"([a-z])([A-Z])"
result = re.sub(pattern,r"\1 \2", text)
print(result) 
#or
print(re.split(r'(?=[A-Z])', "strString"))


#TASK 9

import re
s = "HelloWorld"
spaced = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
print(spaced)


#TASK 10


import re
s = "camelCase"
snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(snake_case)

