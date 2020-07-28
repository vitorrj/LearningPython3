# | ------------------ |
# | --- NESTED LIST -- |
# | ------------------ |

nestedList = [[1,2,3],[4,5]]
nestedList.append('i')
print(nestedList)

### Printing the first list
print(nestedList[0])

### Appending

nestedList[1].append(6)
print(nestedList)

### Changing a value from

nestedList[1][2] = "Changed!"
print(nestedList)

###  Nested dictionary
info = {'personal_data':{
    'name': "Vitor",
    'age':  24,
    'physical_features':{
        'eyes':{
            'color': 'brown',
            'size': 'small'
        },
        'height': 113
        }
    }
}
##### getting a specific item such as the color of the eye
print(info)
print(info['personal_data'])
print(info['personal_data']['physical_features'])
print(info['personal_data']['physical_features']['eyes'])
print(info['personal_data']['physical_features']['eyes']['color'])