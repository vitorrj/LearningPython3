# EXERCISE 1
# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

myfile = open("travel_plans.txt", 'r')

num = len(myfile.read())

# EXERCISE 2
# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words

myfile = open("emotion_words.txt", 'r')

lines = myfile.readlines()
num_words = 0

for line in lines:
    words = line.split()
    num_words += len(words)

### EXERCISE 3
# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars

myfile = open("school_prompt.txt", 'r')

text = myfile.read()
beginning_chars = ""

for char in text[:30]:
    beginning_chars = beginning_chars + char

### EXERCISE 4
# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

myfile = open("school_prompt.txt", 'r')

three = []
lines = myfile.readlines()

for line in lines:
    words = line.split()
    three.append(words[2])

# EXERCISE 5
# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

myfile = open("emotion_words.txt", 'r')

emotions = []
lines = myfile.readlines()

for line in lines:
    words = line.split()
    emotions.append(words[0])

print(emotions)


# EXERCISE 6
# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars