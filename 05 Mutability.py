### Because strings are not mutable, how can I replace a character?

myString = "Hello, World!"
myNewString = "J" + myString[1:]
print(myNewString)