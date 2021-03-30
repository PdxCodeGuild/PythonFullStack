







class ATM:

    def __init__(self):
        self.bal = 0
    
    def balance(self):
        return self.bal
    
    def increment(self):
        self.bal += 1
    

atm = ATM()
print(atm.balance())
atm.increment()
print(atm.balance())

exit()


x = int() # x = 0
print(type(x))
# x += 1

class str:
    def __init__(self):
        ...
    
    def lower(self):
        ...
    
    def upper(self):
        ...
    
    def split(self, delimiter):
        ...

text = str() # y = ''
print(type(text))
text.lower()
text.split(',')

# x = 'hello'
# y = 'goodbye'



atm = ATM()
print(type(atm))







class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def speak(self):
        print('Hello my name is ' + self.name)

pete = Person('Pete', '6\'4"')
pete.speak()

will = Person('Will', '5\'10"')
will.speak()









