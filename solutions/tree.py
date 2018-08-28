# print('    #')
# print('   ###')
# print('  #####')
# print(' #######')
# print('   ##')

#  print('{}{}'.format(' ' * 4, '#'))
#  print('{}{}'.format(' ' * 3, '#' * 3))


# print('\nNEW TREE')
# print('{}{}'.format(' ' * 4, '#' * 1))
# print('{}{}'.format(' ' * 3, '#' * 3))
# print('{}{}'.format(' ' * 2, '#' * 5))
# print('{}{}'.format(' ' * 1, '#' * 7))
# print('{}{}'.format(' ' * 3, '#' * 2))

level = 50
original_level = level
hash = 1

while (level > 0):
    level = level - 1
    print('{}{}'.format(' ' * level, '#' * hash))
    hash = hash + 2

print('{}{}'.format(' ' * (original_level - 2), '#' * 2))
