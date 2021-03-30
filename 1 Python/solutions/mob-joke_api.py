import string
import requests
import json
import time


def get_integer(text, low_bound, upper_bound):
    while True:
        choice = input(text)
        if choice.isdigit():
            choice = int(choice)
            if low_bound <= choice <= upper_bound:
                return choice

catagories = ['Any', 'Miscellaneous', 'Programming', 'Dark', 'Pun', 'Spooky', 'Christmas']
joke_api_base_url = 'https://sv443.net/jokeapi/v2/joke/'
# https://sv443.net/jokeapi/v2/joke/Programming

len_catagories = len(catagories)

for i in range(len_catagories):
    print(f'{i + 1} - {catagories[i]}')


text = f"Here are the possible catagores, select [1-{len_catagories}]:\n"
category_choice = get_integer(text, 1, len_catagories)
selected_catagory = catagories[category_choice - 1]

max_jokes = 10
text = f"How many jokes do you want, select [1-{max_jokes}]:\n"
amount_of_jokes = get_integer(text, 2, max_jokes)
blflag = "nsfw,religious,political,racist,sexist"
params = {'blacklistFlags':blflag, 'amount': amount_of_jokes}

# https://sv443.net/jokeapi/v2/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist
#https://sv443.net/jokeapi/v2/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist&amount=4

newurl = joke_api_base_url + selected_catagory
print(f"New url base: {newurl}")

response = requests.get(newurl, params=params)

#print(response)
print(response.text)
print("\n\n")
jokes_list = json.loads(response.text)
len_returned_jokes = len(jokes_list['jokes'])
jokes = jokes_list['jokes']
for joke in jokes:
    print(joke['setup'])
    time.sleep(3)
    print(joke['delivery'])
    print("\n\n")
    time.sleep(3)