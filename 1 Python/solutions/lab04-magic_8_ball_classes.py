



# from datetime import datetime

# now = datetime.now()
# print(str(now)) # print(now)
# print(repr(now))

# now2 = eval(repr(now))
# print(now2)






# class Magic8BallQuestion:
#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer
    
#     def get_question(self):
#         return self.question

#     def __str__(self):
#         return self.question + ' ' + self.answer
    
#     # def __repr__(self):
#     #     return str(self)



# question1 = Magic8BallQuestion('Will I win the lottery?', 'Definitely')
# question2 = Magic8BallQuestion('Will it be sunny tomorrow?', 'Likely')
# print(question1)
# print(question1.get_question())
# # print(str(question1))
# # print(question1.__str__())




# print(question2)
# print([question1, question2])


import random

class Magic8Ball:

    def __init__(self):
        self.__answers = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Don\'t count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]
        self.__history = []
    
    def ask_question(self, question):
        answer = random.choice(self.__answers)
        self.__history.append({
            'question': question,
            'answer': answer
        })
        return answer
    
    def print_history(self):
        for qa in self.__history:
            print(qa['question'] + ' ' + qa['answer'])


magic_8_ball = Magic8Ball()
# answer = magic_8_ball.ask_question('Will I win the lottery tomorrow?')
# print(answer)
# answer = magic_8_ball.ask_question('Will it be sunny tomorrow?')
# print(answer)
# magic_8_ball.print_history()


while True:
    command = input('Would you like to ask a question, show history, or exit: ')
    if command == 'question':
        question = input('Enter your question: ')
        answer = magic_8_ball.ask_question(question)
        print(answer)
    elif command == 'history':
        magic_8_ball.print_history()
    elif command == 'exit':
        break
    else:
        print('command not recognized')
    





