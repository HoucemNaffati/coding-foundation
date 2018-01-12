import datetime


def write():
    storage = open('water.txt', 'a')
    date_str = str(datetime.datetime.now())
    storage.write(date_str)
    storage.close()


def read():
    storage = open('water.txt', 'r')
    for line in storage.readlines():
        print(line)
    storage.close()


while True:
    print('-' * 40, ' Infamous Water Tracker', '-' * 40)
    print('What do you want to do? [T]rack, [C]heck [Q]uit')
    action = input('').lower()

    if action == 't':
        print('This person tracks!')
        write()
    elif action == 'c':
        print('Here\'s the water you drank:')
        read()
    elif action == 'q':
        break
