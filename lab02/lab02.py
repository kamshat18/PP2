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
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #Python sort
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #Copy list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)   #Join lists
#Python tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")#Acces tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #Update values
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)#Unpack tuple 
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1            #Loop tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)#Join tuples
#PYTHON SETS
set1 = {"abc", 34, True, 40, "male"}
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)#Add set items
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #Remove set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)      #Loop sets
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)   #Join sets
#PYTHON DICTIONARY
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
x = thisdict.get("model") 
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #The popitem() method removes the last inserted item
print(thisdict)
#Access & Change & Add & Remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)#Loop dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}#nested dict
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Python If ... Else
#while loop
i = 1

while i < 6:
  print(i)
  i += 1
#FOR L(OO)PS
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#DONE!!!