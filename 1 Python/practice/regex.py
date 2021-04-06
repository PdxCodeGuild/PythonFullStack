
# Practice 6: Regular Expressions


# Validate an Email Address
# Write a function `validate_email_address` which returns `True` if the given string is an email address, `False` is it isn't.

def validate_email_address(email):
    ...
print(validate_email_address('test@gmail.com')) # True
print(validate_email_address('abc123@gmail.com')) # True
print(validate_email_address('test')) # False
print(validate_email_address('test@gmail')) # False
print(validate_email_address('test@gmail@com')) # False

# Validate a Phone Number
# Write a function `validate_phone_number` which returns `True` if the given string is a phone number, `False` if it isn't.

def validate_phone_number(phone_number):
    ...
print(validate_phone_number('0123456789')) # True
print(validate_phone_number('012-345-6789')) # True
print(validate_phone_number('(012) 345-6789')) # True
print(validate_phone_number('012-3A5-6789')) # False
print(validate_phone_number('1-1-1')) # False


# Clean a Phone Number
# Write a function `clean_phone_number` which returns a string containing just the numbers of a phone number if it's valid, `None` if it's not. Hint: use capture groups.

def clean_phone_number(phone_number):
    ...
print(clean_phone_number('0123456789')) # 0123456789
print(clean_phone_number('012-345-6789')) # 0123456789
print(clean_phone_number('(012) 345-6789')) # 0123456789
print(clean_phone_number('012-3A5-6789')) # None
print(clean_phone_number('1-1-1')) # None

# Find All Numbers
# Write a function `find_numbers` which returns a list of floats found in the given string.

def find_numbers(text):
    ...
text = '''
name  favorite number
joe   1.23
jane  5.45
julie -1.34
bob   4.123
'''
print(find_numbers(text)) # [1.23, 5.45, -1.34, 4.123]

# Parse Query String
# Write a function `parse_query_string` which takes a string representing a [query string](https://en.wikipedia.org/wiki/Query_string) and returns a dictionary containing the contents.

def parse_query_string(qs):
    ...
print(parse_query_string('?a=1&b=2&c=3')) # {'a': 1, 'b': 2, 'c': 3}

# Parse URL
# Write a function `parse_url` which takes a string representing a url and returns a dictionary containing the various parts.

def parse_url(url):
    ...
print(parse_url('https://en.wikipedia.org/wiki/Web_development#Chronology'))
# {
#    'protocol': 'https',
#    'subdomain': 'en',
#    'domain': 'wikipedia.org',
#    'path': '/wiki/Web_development',
#    'fragment': 'Chronology'
# }


