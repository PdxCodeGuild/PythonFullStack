
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    ...

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True



# Percentage
# Write a function that takes two integers, a value and a maximum

def percentage(v, max):
    ...

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'


