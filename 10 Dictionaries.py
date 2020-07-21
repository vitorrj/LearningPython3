# | ------------------ |
# | -- DICTIONARIES -- |
# | ------------------ |

# Dictionaries are unordered lists that has a key-value pairs
mydict = {"one": 1, "two": 2}
mydict["three"] = 3                         # alternative way of assigning key-value pairs
print(mydict)

### Passing a value from dictionary to a variable
value = mydict["one"]
print(value)

print(mydict.get("one"))                   # alternative way of accessing a key

### Deleting a value
del mydict["three"]
print(mydict)

### Getting a list of keys
mydict = {'apples': 32, 'oranges': 14, 'pears': 69, 'bananas': 2}

mykeys = list(mydict.keys())
print(mykeys)                                                      # ['apples', 'oranges', 'pears', 'bananas']

for key in mydict:
    print("{} has the value of {}".format(key,mydict[key]))         # looping all keys, it doesn't return a list

### Returning a list of the values
myvalues = list(mydict.values())
print(myvalues)


### Returning the pairs
mypairs = list(mydict.items())
print(mypairs)

### Getting a value                               # gets returns the value associated with a given key
print(mydict.get('apples'))                      # 32
print(mydict.get('watermelon'))                  # None
print(mydict.get('watermelon', "Not found!"))    # "Not found!". I can set a response in case .get() returns None

### Accumulating values to a dictionary
myfile = open("assets/myfile.txt", 'r')
text = myfile.read()

mydict = {}                                       # empty dictionary

for char in text:
    if char not in mydict:                        # if the key doesn't exist, create one
        mydict[char] = 0
    mydict[char] += 1

print(mydict)