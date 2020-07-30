# Questions
# 1. What is the baseurl?
# 2. What keys should you provide in the dictionary you pass for the params parameter?
# 3. What values should you provide associated with those keys?
# 4. Do you need to authenticate yourself as a licensed user of the API and, if so, how?
# 5. What is the structure and meaning of the data that will be provided?


import requests
import json

### Setting up a variable for the API
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")

requestsParameters = {'rel_rhy': 'funny'}                               # passing parameters as dictionary
page2 = requests.get("https://api.datamuse.com/words", params = requestsParameters)

### Passing to text
print(page.text[:94])
print(page.url)
print(page2.text[:94])                                                  # same request
#print(textFromPage)

### or alternatively we can parse in json
textFromPageInJson = page.json()
print(type(textFromPageInJson))
print(len(textFromPageInJson))
#print(json.dumps(textFromPageInJson, indent=2))
