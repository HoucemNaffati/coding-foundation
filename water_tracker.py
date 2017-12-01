import datetime

tracking = []

while True:
    print('-' * 40, ' Infamous Water Tracker', '-' * 40)
    print('What do you want to do? [T]rack, [C]heck')
    action = input('').lower()
    if action == 't':
        print('Cool! Thanks for letting me know, I\'ll store that for you!')
        tracking.append(datetime.datetime.now())
    elif action == 'c':
        print('Here\'s the water you drank:')
        for cup in tracking:
            print('- {}'.format(cup))
