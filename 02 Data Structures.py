### LISTS
mylist = [24, "apple", 1984.0, "vitor"]
print(mylist[-1])           # "vitor" the last element of the list
print(len(mylist))          # 2 elements

### TUPLES
mytupple = (1,3,4)

print(mytupple)

##### How to slice a string or or list?
print(mylist[1:3])          # "apple" + 1984.0

##### Repeat elemnts of a list?
repeatedlist = [0] * 4      # [0, 0, 0, 0]
print(repeatedlist)

##### Print last digits of an array
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
print(sports[-3:])

### COUNT and INDEX"
print("COUNT AND INDEX")
text = "My name is Vitor. Rodrigues"
print(text.count("i"))          # 3 because we have 3 i
print(text.index("is"))         # the position of the word 'is'

myarray = [1,1,3,2,1,1,1,46,4,6]
print(myarray.count(1))
print(myarray.index(3))

name = "vitor"
print(name[1:3])



