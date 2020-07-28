# | ------------------ |
# | -- MAP AND FILTER- |
# | ------------------ |

# MAP
# working on lists

mylist = [1,2,3]

def triple(value):
    return value*3

def tripleList(mylist):
    new_list = map(triple, mylist)                # map(functiion, list)
    print(new_list)                               # <map object at 0x7fb1cbf9ce20>
    return list(new_list)

print(tripleList([2,3,4]))                       # [6, 9, 12]

### Mapping with lambda function
mynewlist = list(map(lambda x: x*4,mylist))           # fancier way using lambda function
print(mynewlist)

# FILTER
# returning only item I want

mynewlist = list(filter(lambda num: num%2 == 0, mylist))    # returning only even numbers
print(mynewlist)

# LIST COMPREHENSIONS
# alternative to map and filter
print("----- LIST COMPREHENSIONS ------")

### mapping with list comprehensions                    # [<transform expression> for <var> in <mylist>]
mynewlist = [value*2 for value in mylist]
print(mynewlist)

### filter with list comprehensions
mynewlist = [value for value in mylist if value%2 == 0]
print(mynewlist)

### zip and list comprehesion
list1 = [1,2,3]
list2 = [3,4,5]

sumlist =[x+y for x,y in zip(list1,list2)]
print(sumlist)