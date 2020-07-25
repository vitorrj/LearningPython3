mylist = [1,2,3]
print("------ My list ------ \n", mylist, "\n---------------------\n")


### Adding items to the llist
mylist.append(2020)                 # it's the same as concatenation mylist = mylist + [2020]
print(mylist)                       # [1, 2, 3, 2020]

### Inserting an item in any position?
mylist.insert(1,1996)
print(mylist)                       # [1, 1996, 2, 3, 2020]

### Reversing the list METHOD
mylist.reverse()
print(mylist)                       # [2020, 3, 2, 1996, 1]

### Checking where an element is
print(mylist.index(1996))               # 3 because it is the position of 1996

### Deleting any element of the list
mylist.remove(2020)
print(mylist)

### Deleting the last element
mylist.pop()
print(mylist)

### Sorting a list METHOD
randomlist = [4,1,5]
randomlist.sort()
print(randomlist)                       # [1, 2, 3, 1996, 2020] changes the original list
print(randomlist.sort())

randomlist = [4,1,5]
mynewlist = sorted(randomlist)
print(mynewlist)

### Reverse sorting
print(sorted(mynewlist, reverse = True))