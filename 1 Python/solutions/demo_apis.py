

import requests

# response = requests.get('https://github.com/PdxCodeGuild/class_bumble_bee/blob/main/0%20General/08%20-%20Networking.md')
# print(response.text)


# response = requests.get('https://random-word-api.herokuapp.com/word?swear=0')
# print(response.text)

# json.loads turns a string containing json into a python list or dictionary
# import json
# print(json.loads(response.text)[0])

# print(response.json()[0])




# dad joke api: https://icanhazdadjoke.com/api
# ============================================

# get a random dad joke
# response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
# response_data = response.json() # {'id': 'kqcFBlGJYDd', 'joke': 'You know what they say about cliffhangers...', 'status': 200}
# print(response_data['joke'])



# term = input('what is the term you\'d like to search for? ')
# response = requests.get('https://icanhazdadjoke.com/search?term=' + term, headers={'Accept': 'application/json'})

# params is the query string
term = input('what is the term you\'d like to search for? ')
response = requests.get('https://icanhazdadjoke.com/search', headers={'Accept': 'application/json'}, params={'term': term})

# json visualizer: http://jsonviewer.stack.hu/
# print(response.text)


response_data = response.json()
# print(response_data['results'][0]['joke'])
for result in response_data['results']:
    print(result['joke'])



response = requests.get('https://favqs.com/api/qotd')
print(response.text)