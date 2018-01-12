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
