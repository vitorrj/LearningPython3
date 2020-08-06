# JSON stands for JavaScript Object Notation
import json


### Writing to JSON (loads)
a_string  =  '{ "name":"Vitor", "age":24, "city":"Naples"}'
myDict = json.loads(a_string)
print(myDict)


### Reading JSON (dumps)
dict = {'key1':{'a':1,'b':2,'c':3}, 'key2':{'d':4, 'e':5, 'f':6}}

textJson = json.dumps(dict, sort_keys= True, indent = 2)
print(type(textJson))
print(textJson)
