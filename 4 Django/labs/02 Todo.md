# Lab 2: Todo

## Part 1

Let's create a simple todo app. This can be done with a two models for representing a `TodoItem` and `Priority`. Newly created `TodoItem`s should have a `null` completed date. The index page should have a list of all the todo items (showing only the name), with completed items in a separate list (or at the bottom of the existing list) with grey color and maybe a line through them. There should also be a text field and a button (in a form), When the clicks the button it should saves a new todo item to the database and shows the newly-added item in the list. The form for creating a todo item should also have a dropdown list for selecting the priority. Use one view to render the template, and another view to receive the form submission and redirect back to the first view.


### Steps

1. Create the project and app
2. Create the index view and route to get there, test it to make sure you can complete a request-response cycle
3. Create your models, run migrations, log into your admin panel and enter some information (test CRUD)
4. Go back to your index view, get data out of the database and render it in a template
5. Create the form in your template, create a save_todo_item view, make sure your form data is received by the view (`print(request.POST)`)
6. Using the form data, create an instance of your TodoItem model, save it, and redirect back to the index page


### Models

- Priority
  - name - CharField (high, medium, low)

- TodoItem
  - text - CharField
  - priority - ForeignKey to Priority
  - created_date - DateTimeField
  - completed_date - DateTimeField (nullable)


### Views

- Index Page
  - List of the uncompleted todo items including text, priority, and created date
  - List of completed todo items including text, priority, and completed date
  - Form for creating a new todo item

- Save Todo Item
  - Receive the form submission and create a new todo item, then redirect back to the first view

## Part 2

Add `complete` and `delete` buttons next to each todo item, these can be `a` tags which link to other views which take the `id` of the todo item in the path. These views can now redirect back to the first view.

