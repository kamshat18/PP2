#lab02
#START:BOOLEANS
print(bool(0))
print(bool("")) ,print(bool("Hello"))
#Python Operators
print(6 & 2 + 1)
print((6 + 3) - (6 + 3))
#Python Lists
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Access Items
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #Change List Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)# Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #Remove List Items
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)#Python - List Comprehension