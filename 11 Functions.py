# | ------------------ |
# | ---- FUNCTIONS --- |
# | ------------------ |

# QUESTIONS
# 1) How many parameters
# 2) What are the types of my parameters?
# 3) What does it return?

### Creating a void function
def myfunction():
    """Docstring about my code"""
    print("Hello word")

myfunction()

### Creating a parameter function
def myfunction(x,y):
    return x+y

sum = myfunction(2,6)
print(sum)

##### terrible function
def myfunction(x,y):
    print(x+y)                 # Doesn't do anything

sum = myfunction(2,6)
print(sum)

### Returning multiple values with tuple packing
def myfunction(x,y):
    a = x + y
    b = x * y
    return a,b                          # alternatively I can use (a,b)

print(myfunction(2,8))

### Unpacking tuples
def myfunction(x,y):
    return x+y

mytupple = (1,4)
print(myfunction(*mytupple))            # tupple unpacking
