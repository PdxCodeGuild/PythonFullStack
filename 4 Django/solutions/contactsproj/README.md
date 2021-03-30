

# Contacts

## Models

- ContactType
  - Name
- Contact
  - First Name (CharField)
  - Last Name (CharField)
  - Email (CharField)
  - Image (ImageField)
  - Birthday (DateField)
  - Type (ForeignKey to ContactType)
  - User (ForeignKey to User)

## Pages

- Home (list of contacts)
- Register
- Login
- Create Contact
- Edit Contact

## User Management Features We'll Use

- The model we'll use: `from django.contrib.auth.models import User`
- Creating a user: `user = User.objects.create_user('jane', 'jane@gmail.com', 'janespassword')`
- Authenticating: `user = authenticate(request, username=username, password=password)`
- Login: `login(request, user)`
- Logout: `logout(request)`
- Only allowing a user to access a page if they're logged in: `@login_required`



