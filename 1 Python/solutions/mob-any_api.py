


import requests
import random
from colorama import Fore, Back, Style

categories = {
    9: 'General Knowledge',
    10: 'Entertainment: Books',
    11: 'Entertainment: Film',
    12: 'Entertainment: Music',
    13: 'Entertainment: Musicals & Theatres',
    14: 'Entertainment: Television',
    15: 'Entertainment: Video Games',
    16: 'Entertainment: Board Games',
    17: 'Science & Nature',
    18: 'Science: Computers',
    19: 'Science: Mathematics',
    20: 'Mythology',
    21: 'Sports',
    22: 'Geography',
    23: 'History',
    24: 'Politics',
    25: 'Art',
    26: 'Celebrities',
    27: 'Animals',
    28: 'Vehicles',
    29: 'Entertainment: Comics',
    30: 'Science: Gadgets',
    31: 'Entertainment: Japanese Anime & Manga',
    32: 'Entertainment: Cartoon & Animations'
}
print('Categories') #Show the user the possible categories as options
for x in categories: # Iterating through the keys in the dictionary 
    print(f'{x-8} - {categories[x]}') #subtract 8 from initial key for readability 
category_selection = int(input(f'Please select category [1-{len(categories)}]: ')) #adding len() to category list for dynamic category list
print(categories[category_selection + 8]) # accessing the dictionary from the users category selection and adding +8 to match website
number_questions = int(input(f'How many questions do you want? [1-10]: ')) # finding the amount  of questions for our parameters                                                      
params_data = {'amount':number_questions,'category': category_selection + 8 }# customizing URL for user's input

score = {'yes': 0, 'no': 0} 
url = "https://opentdb.com/api.php" # Base URL  
response = requests.get(url,params=params_data) #calling the URL
response = response.json() #convertin response to dict python
results = response['results'] #extracting questions from response data & assigning to variable
for result in results:
    print(result['question'])
    #combine incorrect and correct answers in single 'answers' list and shuffling answers
    answers = []
    correct_answer = result['correct_answer']
    incorrect_answers = result['incorrect_answers']
    for answer in incorrect_answers:
        answers.append(answer)
    answers.append(correct_answer)
    random.shuffle(answers)
    #print answers with numbers 
    for i in range(len(answers)):
        print(f'{i+1} {answers[i]}')
    # grabbing the user answer and ensuring it's valid
    while True:
        user_answer = int(input('What is your answer? please select [1-4]'))
        if user_answer in [1,2,3,4]:
            break
    # printing results to the user
    if correct_answer == answers[user_answer-1]:
        print(Fore.GREEN +'Correct,' + Fore.BLUE + 'You\'re a genius!!')
        print(Style.RESET_ALL)
        score['yes'] += 1
    else:
        print(Fore.RED + f'Incorrect! the correct answer is {correct_answer} Get good')
        print(Style.RESET_ALL)
        score['no'] += 1
    print('___________________________')
    #number of questions that have been asked of the user
print(f'You got {score["yes"]} out of {score["yes"] + score["no"]} questions correct')