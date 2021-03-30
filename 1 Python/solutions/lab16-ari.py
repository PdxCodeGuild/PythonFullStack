

import re
import requests
import string

def load_text():

    book_url = 'http://www.gutenberg.org/cache/epub/1065/pg1065.txt'
    response = requests.get(book_url)
    response.encoding = 'utf-8'
    text = response.text
    
    beginning_junk_index = text.find('*** START OF THIS PROJECT GUTENBERG')
    beginning_junk_index = text.find('\n', beginning_junk_index)
    end_junk_index = text.find('End of the Project Gutenberg EBook')
    text = text[beginning_junk_index:end_junk_index]

    return text


def count_characters(text):

    # for punc in string.punctuation + string.whitespace + string.digits:
    #     text = text.replace(punc, '')
    # return len(text)

    # count = 0
    # for char in text:
    #     if char in string.ascii_letters:
    #         count += 1
    # return count

    # letters = [char.lower() for char in text if char in string.ascii_letters]
    # return len(letters)


    return len(re.findall(r'[a-zA-Z]', text))



def count_words(text):

    results1 = re.findall(r"[\w']+", text)
    
    # text = text.replace('--', ' ')
    # results2 = text.split()

    return len(results1)



def count_sentences(text):

    # count whole sentences
    # https://regex101.com/r/ELyRzI/1

    results = re.findall(r"[.!?]+", text)
    return len(results)

    # counter = 0
    # for char in text:
    #     if char in ['.', '!', '?']:
    #         counter += 1
    # return counter



text = load_text()
num_characters = count_characters(text)
num_words = count_words(text)
num_sentences = count_sentences(text)





