
import random
import string
import requests

class PasswordGenerator:

    def __init__(self):
        pass
    
    def generate_password(self):
        return ''



class SimplePasswordGenerator(PasswordGenerator):

    def __init__(self, num_characters):
        self.num_characters = num_characters
    
    def generate_password(self):

        # return ''.join([random.choice(string.ascii_letters) for i in range(n)])

        output = ''
        for i in range(self.num_characters):
            output += random.choice(string.ascii_letters)
        return output


class ComplexPasswordGenerator(PasswordGenerator):

    def __init__(self, num_lowercase, num_uppercase, num_digits, num_special):
        self.num_lowercase = num_lowercase
        self.num_uppercase = num_uppercase
        self.num_digits = num_digits
        self.num_special = num_special
    
    def generate_password(self):
        output = []
        output.extend(random.sample(string.ascii_lowercase, self.num_lowercase))
        # for i in range(self.num_lowercase):
        #     output.append(random.choice(string.ascii_lowercase))
        output.extend(random.sample(string.ascii_uppercase, self.num_uppercase))
        output.extend(random.sample(string.digits, self.num_digits))
        output.extend(random.sample(string.punctuation, self.num_special))
        random.shuffle(output)
        return ''.join(output)


class WordPasswordGenerator(PasswordGenerator):

    def __init__(self, num_words):
        self.num_words = num_words

    def generate_password(self):
        response = requests.get('https://random-word-api.herokuapp.com/word', params={'number': self.num_words, 'swear': 0})
        words = response.json()
        return ' '.join(words)
        

# pg = SimplePasswordGenerator(10)
# pg = ComplexPasswordGenerator(5, 5, 5, 5)
pg = WordPasswordGenerator(5)
while True:
    password = pg.generate_password()
    print(password)
    another_password = input('Would you like another password? ').lower().strip()
    if another_password not in ['y', 'yes', 'yup', 'yeah']:
        break




