


# MadLib


## Views

- index
  - render the index template
  - show a list of madlib titles, clicking one takes you to the detail page
- detail
  - show input fields for the words for a given madlib
- result
  - receive the form submission
  - show the result of the madlib

## Models

- MadLib
  - title (CharField)
  - template (TextField)
- MadLibWord
  - madlib (ForeignKey)
  - variable name (CharField)
  - part of speech (CharField)

