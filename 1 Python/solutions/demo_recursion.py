


# iterative factorial

def factorial(n):
    output = 1
    for x in range(1, n+1):
        output *= x
    return output


# print(factorial(5))  # 5*4*3*2*1 = 120


# a recursive function is a function that calls itself


# f(5) = 5*f(4)                      = 5*4*3*2*1*1
#    f(4) = 4*f(3)                = 4*3*2*1*1
#       f(3) = 3*f(2)           = 3*2*1*1
#         f(2) = 2*f(1)      = 2*1*1
#           f(1) = 1*f(0) = 1*1
#              f(0) = 1



def factorial_recursive(n):
    if n == 0: # base case
        return 1
    return n*factorial_recursive(n-1) # recursive call

# print(factorial_recursive(5))  # 5*4*3*2*1 = 120







def fibonacci(n):
    output = []
    for i in range(n):
        if i == 0 or i == 1:
            output.append(1)
        else:
            output.append(output[i-1] + output[i-2])

    return output

print(fibonacci(5))



# f(5)
# f(4) + f(3)
# f(3) + f(2) + f(3)
# f(2) + f(1) + f(2) + f(3)
# f(1) + f(0) + f(1) + f(2) + f(3)


global counter
counter = 0

def fibonacci_recursive(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for n in range(1,21):
    counter = 0
    fibonacci_recursive(n)
    print(n, counter)
