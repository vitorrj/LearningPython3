# Assingment from week 2 https://fopp.umsi.education/assignments/doAssignment?assignment_id=6

# Exercise 1

my_str = "MICHIGAN"

for str in my_str:
    print(str)

### Exercise 2
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for elements in several_things:
    print(elements)

for elements in several_things:
    print(type(elements))

### Exercise 3
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for elements in str_list:
    print(len(elements))

### Exercise 4
original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for _ in original_str:
    num_chars += 1
print(num_chars)

### Exercise 5
addition_str = "2+5+10+20"
sum_val = 0

for value in addition_str.split("+"):
    sum_val += int(value)

print(sum_val)

### Exercise 6
# week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

temps = week_temps_f.split(",")             # returns me the list with the elements
avg_temp = 0

for currentTemp in temps:
    avg_temp += float(currentTemp)         # add and convert from str to float
avg_temp = avg_temp/len(temps)             # divide by the amount of elements

print(avg_temp)


### Exercise 7

nums = list(range(68))
print(nums)

###  Exercise 8

original_str = "The quick brown rhino jumped over the extremely lazy fox"
listString = original_str.split()                   # creates a list with the elements of original_str
num_word_list = [0] * len(listString)               # initialize my with with the lenght of words
count = 0

for str in listString:
    num_word_list[count] = len(listString[count])
    count += 1

print(num_word_list)

### Exercise 9

lett = ""
for _ in range(7):
    lett += "b"
print(lett)