tester = {'info': [
    {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
    {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
    {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
    {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
    {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
    {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]
}


print(tester.keys())
myInformation = tester['info']
print(myInformation[0])

compri = [print(key) for key in myInformation if key == 'name']


compri = [key['name'] for key in myInformation]
print(compri)
