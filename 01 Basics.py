### DECLARATION
name = "vitor"
age  = 24.0

### OPERATORS
print(2 ** 3)               # 8
print(10 // 3)              # returns an integer = 3

### VARIABLE METHODS
type(name)
len(name)
print(type(name),len(name))           # returns <class 'str'> and the size of name

### MANIPULATING STRINGS
print("Vitor's Pub")                                        # Using "" to produce ''
print('"Vitor said something"')                             # Using '' to product ""
print(''''Vitor "said" something about Vitor's Pub''')      # Using ''' to produce "" and ''

### CONVERTING DATA TYPES
print(int(age))             # float to int, returns 24
print(type(str(1107.16)))   # converts 1107.16 into an string and returns the type


### GETTING INPUTS FROM USER
name = input("\nWhat is your name?")
print("Your name is " + name)

rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""
print(len(rv))