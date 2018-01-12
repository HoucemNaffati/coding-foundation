import random


bullet_chamber = random.randint(1, 6)
players = ['player 1', 'player 2', 'player 3', 'player 4']

current_player_index = 0

chambers = range(1, 7)
for chamber in chambers:
    current_player = players[current_player_index]

    current_player_index += 1
    if current_player_index >= len(players):
        current_player_index = 0

    print(
        '{} grabs the guns, places in his head and Clicks...'
        .format(current_player)
    )
    input()
    if chamber == bullet_chamber:
        print('{} lost :('.format(current_player))
        break
    else:
        print('{} can continue the game...'.format(current_player))
