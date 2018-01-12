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
