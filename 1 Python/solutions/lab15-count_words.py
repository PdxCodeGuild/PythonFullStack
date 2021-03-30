
import requests
import string
import re

book_url = 'http://www.gutenberg.org/cache/epub/1065/pg1065.txt'
response = requests.get(book_url)
response.encoding = 'utf-8'

text = response.text

beginning_junk_index = text.find('*** START OF THIS PROJECT GUTENBERG')
beginning_junk_index = text.find('\n', beginning_junk_index)
end_junk_index = text.find('End of the Project Gutenberg EBook')
text = text[beginning_junk_index:end_junk_index]

words = text.split()
words = [word.lower() for word in words] # make lower case
words = [word.strip(string.punctuation) for word in words] # strip punctuation

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        # word_counts.update({word: 1})


# word_counts = {}
# for word in words:
#     word_counts[word] = word_counts.get(word, 0) + 1




# text = text.replace('.', ' ')
# text = text.replace('-', ' ')

# for punctuation in string.punctuation:
#     text = text.replace(punctuation, ' ')

# print(text.split())


# print(re.findall('[\\w\']+', text))


