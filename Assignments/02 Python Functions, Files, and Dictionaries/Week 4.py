# EXERCISE 1
# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(mylist):
    count = 0
    newlist = []
    while mylist[count] != 5:
        newlist.append(mylist[count])
        count += 1
    return newlist

mylist = [1,2,4, 20, 5]
newlist = sublist(mylist)
print(newlist)

# EXERCISE 2
# Write a function called check_nums that takes a list as its parameter, and contains a while loop
# that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(mylist):
    count = 0
    mynewlist = []
    while mylist[count] != 7:
        mynewlist.append(mylist[count])
        count += 1
    return mynewlist

# EXERCISE 3
# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(list_string):
    newlist = []
    count = 0
    while list_string[count] != "STOP":
        newlist.append(list_string[count])
        count += 1
    return newlist

# EXERCISE 4
# Write a function called stop_at_z that iterates through a list of strings.
# Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(string_list):
    newlist = []
    count = 0
    while string_list[count] != 'z':
        newlist.append(string_list[count])
        count += 1
    return newlist



# EXERCISE 5
# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop.
# Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
count = 0
while count < len(lst):
    sum2 += lst[count]
    count += 1

# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’.
# What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element,
# the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(mylist):
    count = 0
    newlist = []

    while mylist[count] != "bye":
        if count == 10:
            break
        else:
            newlist.append(mylist[count])
            count += 1
    return newlist


