# EXERCISE 1
# Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"

sorted_letters = sorted(letters, reverse = True)

# EXERCISE 2
# Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)

# EXERCISE 3
# The dictionary, medals, shows the medal count for six countries during the Rio Olympics.
# Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical = sorted(medals)


# EXERCISE 4
# Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

medals_sorted = sorted(medals, key = lambda k: medals[k], reverse = True)
print(medals_sorted)

top_three = []
for key in medals_sorted[:3]:
    top_three.append(key)
print(top_three)

# EXERCISE 5
# We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values,
# from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed = sorted(groceries, key = lambda  k: groceries[k], reverse = True)



# EXERCISE 6 | HARD!!!
# Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005.
# Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest.
# Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
def last_four(number):
    new_number = str(number)
    return new_number[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key = last_four)
print(sorted_ids)


# EXERCISE 7 | HARD!!!
# Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

ids_string = []

for id in ids:
    ids_string.append(str(id))
print(ids_string)

sorted_ids = sorted(ids_string, key = lambda char: char[-4:])
print(sorted_ids)

# EXERCISE 8
# Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.

ex_lst =['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda char: char[1])
print(lambda_sort)