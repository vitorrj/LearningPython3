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


# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #
# EXERCISE 1
# Create a function called mult that has two parameters, the first is required and should be an integer,
# the second is an optional parameter that can either be a number or a string but whose default is 6.
# The function should return the first parameter multiplied by the second.
def mult(number1, number2= 6):
    return number1 * number2


# EXERCISE 2
# The following function, greeting, does not work. Please fix the code so that it runs without error.
# This only requires one change in the definition of the function.
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


# EXERCISE 3
# Below is a function, sum, that does not work. Change the function definition so the code works.
# The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
def sum(intx, intz=5):
    return intz + intx

# EXERCISE 4
# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True,
# and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see
# if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(number, bool = True, dict1 = {2:3, 4:5, 6:8}):
    keys = list(dict1.keys())
    print(keys)
    if bool == True:
        for key in dict1:
            if key in keys:
                bool = True
                return dict1.get(key)
    else:
        bool = False
        return bool

print(test(2))

# EXERCISE 5
# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string.
# The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of
# {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True,
# it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
# But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(string, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7} ):
    keys = list(d.keys())
    print(keys)
    if direction == True:
        if string in keys:
            return True
        else:
            return False
    elif direction == False:
        if string not in keys:
            return True
        else:
            return False


# EXERCISE 6
# We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that
# value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.
---
