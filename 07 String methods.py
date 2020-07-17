mystring = "    Hello, World!     "
print("---------------- \n", mystring, "\n-----------------\n")

### reversing string
stringreversed = mystring[::-1]
print(stringreversed)
### All caps
print(mystring.upper())                #     HELLO, WORLD!

### All lower
print(mystring.lower())                #     hello, world!

### Count element
print(mystring.count("l"))             # 3

### Removing whitespaces
newstring = mystring.strip()
print(newstring)                # Hello, World! It removes the whitespaces

### Replacing iems
newstring = newstring.replace("l", "!!!")    # I need to create a new one because strings are immutable
print(newstring)                            #     He!!!!!!o, Wor!!!d!

### Alternative way of passing variables to a string
name = "Vitor"
print(name + ", you are an amazing person!")            # Ugly

print("{}, you are an amazing person!".format(name))    # Beautfil