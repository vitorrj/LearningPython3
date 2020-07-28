# JSON stands for JavaScript Object Notation

import json


### Writing to JSON (loads)
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
dict_json  = json.loads(a_string)
print(dict_json)
print(type(dict_json))


### Reading JSON (dumps)
dict = {'key1':{'a':1,'b':2,'c':3}, 'key2':{'d':4, 'e':5, 'f':6}}

dict_json = json.dumps(dict, sort_keys= True, indent = 2)
print(dict_json)
