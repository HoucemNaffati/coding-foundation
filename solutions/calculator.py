first = int(input('First number: '))
second = int(input('First second: '))
option = input('What to do? (+ or -)? ')

if option == '+':
    total = first + second
    print('{} + {} = {}'.format(first, second, total))
elif option == '-':
    total = first - second
    print('{} - {} = {}'.format(first, second, total))
elif option == 'x':
    total = first * second
    print('{} x {} = {}'.format(first, second, total))
elif option == '%':
    total = first / second
    print('{} % {} = {}'.format(first, second, total))
else:
    print('You wot m8?')


# #######################################

































first = int(input('First number: '))
second = int(input('First second: '))
option = input('What to do? (+ or -)? ')

if option == '+':
    total = first + second
elif option == '-':
    total = first - second
elif option == 'x':
    total = first * second
elif option == '%':
    total = first / second
else:
    print('You wot m8?')

print('{} {} {} = {}'.format(first, option, second, total))

############################################################################













































first = int(input('First number: '))
second = int(input('First second: '))
option = input('What to do? (+ or -)? ')

def sum(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

if option == '+':
    total = sum(first, second)
elif option == '-':
    total = subtract(first, second)
elif option == 'x':
    total = multiply(first, second)
elif option == '%':
    total = divide(first, second)
else:
    print('You wot m8?')

print('{} {} {} = {}'.format(first, option, second, total))
