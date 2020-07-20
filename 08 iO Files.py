# READING FILES

path = "assets/myfile.txt"          # for absolute path we use "../"
print("------ HEADING ------")

### getting everything on the file
myfile = open(path, 'r')          # holds a reference to the object which is the file
text = myfile.read()
print(text)
myfile.close()

### getting each line
myfile = open(path, 'r')
textlines = myfile.readlines()
print(textlines)                            # returns a list where each line is an element
print(len(textlines))                       # return the number of lines
myfile.close()

### printing all lines
myfile = open(path, 'r')
for line in myfile:
    print(line)

# WRITING FILES
print("------ WRITING ------")

### writing
# myfile = open(path, "w")                          # if the file does not exist, it will create one
# myfile.write(myfile + "Ciao, mondo!")
# myfile.close()

### avoiding .close() and using with

with open(path, 'r') as myfile:                     # 'with' makes easier to open files
    for text in myfile:
        print(text)

