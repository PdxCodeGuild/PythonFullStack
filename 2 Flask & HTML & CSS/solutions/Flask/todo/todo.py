from flask import Flask, render_template, request, redirect

from jsondb import JsonDB

# create a new flask app
app = Flask('todo')

# class which reads and writes from a .json file
db = JsonDB('./db.json')
db.load()

# index page which renders a template with todo items
@app.route('/')
def index():
    return render_template('index.html', todos=db.data['todos'])

# a view which receives a form submission
# and saves a todo item to the database
@app.route('/addtodo/', methods=['GET', 'POST'])
def addtodo():
    print(request.form)
    todo = {
        'text': request.form['text'],
        'priority': request.form['priority']
    }
    db.data['todos'].append(todo)
    db.save()
    return redirect('/')

app.run()
