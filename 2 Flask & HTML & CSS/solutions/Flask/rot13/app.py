
import string
from flask import Flask, render_template, request

def encrypt(text):
    alpha = string.ascii_lowercase # our alphabet is in a string
    rotated = "nopqrstuvwxyzabcdefghijklm" # don't forget that strings have indices as well.
    output1 = [] # make a blank list to add the rorated characters. This will be converted to a string before we return it.
    for char in text: # iterate over the text. start with the h, then e, and so on.
        x = alpha.find(char) # the x variable will hold the index of the letter.
        output1.append(rotated[x]) # add the rotated character to the output1 list
    output = "".join(output1) # conver the output1 list into a string
    return output  # print the string with the converted letters.

app = Flask('rot13')

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ''
    if request.method == 'POST':
        # print(request.form)
        original_text = request.form['original_text']
        encrypted_text = encrypt(original_text)
    return render_template('index.html', encrypted_text=encrypted_text)


app.run()




