# Contact List
django + bootstrap

## Models
-------

City
- name (Portland)
- state (Oregon)
- timezone (stretch goal)

Contact
- id
- first name - charfield
- middle name - charfield (optional - blank=True)
- last name - charfield
- email - charfield
- phone number - charfield
- city id - foreign key to City
- notes - textfield
- created date


## Pages
-------

index page
- list contacts in a table
- name, email, link to the detail page

create page
- form with all the contact fields for the user to fill out

detail page
- show all the contact fields