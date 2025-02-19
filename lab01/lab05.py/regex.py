"""#TASK1
import re
def match_str(s):
    pattern = r'^ab*$'
    return re.search(pattern,s)
test=["bac","ab","abb"]
for x in test:
    print(match_str(x))
"""
#TASK2
import re
"""def matching(s):
    pattern = r'^ab{2,3}$'
    return re.search(pattern,s)  
test=["bac","ab","abb","abbb"]
for x in test:
    print(matching(x))
"""

#TASK 3
"""def Match(s):
    pattern = r'[a-z]+_[a-z]'
    return re.search(pattern,s):
test=["bac","ab","ab_ba","a_b"]
for x in test:
    print(Match(x))"""

#TASK 4
"""def m(s):
    pattern =r'[A-Z][a-z]+'
    return re.search(pattern,s)
       
test=["Az","az","aZ","Azzzz"]
for x in test:
    print(m(x))
"""
#TASK 5
"""def m(s):
    pattern =r'^a\wb$'
    return re.search(pattern,s)
       
test=["bac","a1b","ab_ba","a_b"]
for x in test:
    print(m(x))
"""