



x = 5

def say_hello(name):
    print('hello ' + name + '!')
    x = 2
    print(x)

def main():
    name = input('what is your name? ')
    say_hello(name)
    print('goodbye')
    print(x)


main()
print(x)

