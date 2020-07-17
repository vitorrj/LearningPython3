### Because strings are not mutable, how can I replace a character?

myString = "Hello, World!"
myNewString = "J" + myString[1:]
print(myNewString)

# CREATE FROM HERE
### How can I delete items from a list?
print("------ Deleting items from list ------")

mylist = [1,2,4,5,6,7,8,9,10]
del mylist[:4]
print(mylist)                          # [6, 7, 8, 9, 10]

### How to check if two immutables objects are equal?
##### It works with only immutable objects and returns True
name1 = "Vitor"
name2 = "Vitor"
print(name1 is name2)                   # True
print(id(name1),id(name2))              # They are the same object

##### Doesn't work with lists
mylist1 = [80,81,82]
mylist2 = [80,81,82]
print(mylist1 is mylist2)               # False
print(id(mylist1), id(mylist2))         # They are the same object

mytupple1 = (80,81,82)
mytupple2 = (80,81,82)
print(mytupple1 is mytupple2)               # False

### How to clone two lists?
print("------ Cloning two lists ------")

a = [1,2,3]
b = a
print(a is b)                       # True

b = a[:]
print(a is b)                       # False
