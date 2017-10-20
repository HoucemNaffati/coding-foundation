# Make the computer read your mind

## Problem

The user pick a number between 1 and 10. The program has to guess the number
and ask the user whether the guessed number is correct.


```python
import random

print('User, please pick the number!')
print('I start to guess!')

# The range gives the list of numbers, where range(a, b) a <= n < b
choices = list(range(1,11))

playing = True
while playing:

    guess = random.choice(choices)
    print('My guess is:', guess)

    answer = input('Is it correct? (yes/no): ')
    print('Your answer is:', answer)

    if answer == 'yes':
        playing = False
        print('Game Over!')
    else:
        print('Ok, let me guess again')
        choices.remove(guess)

        # After we removed the last number we know for sure, the user
        # tried to cheat
        if len(choices) == 0:
            print('You are cheating!!!!')
            playing = False
```


## Homework 1

Let's assume the user doesn't cheat. So if the program only has 1 more
choice, it can safely say that the correct answer is the last one.

hint: Modify the existing condition, where we detect the cheating.

### Questions

If the range is from 1 to 100, and we pick random numbers why is the average of guesses 50?

## Homework 2

Modify the range from 1 to 10 to 1 to 100. The game will take as much time
as the computer need to guess 50 numbers in average to be able to guess
the correct number.
Because the nature of the list is ordered, the program can use a different
approach and ask whether the number in the user's mind lower, higher or correct.

hint (1):
    Ask the user "Is the number lower, higher or correct? (lower/higher/correct)"
    instead of asking a yes/no question.
hint (2):
    If the guess isn't correct, remove the guess and all of the other incorrect
    numbers too.
hint (3):
    You might want to replace the random number picking with something more
    efficient.

### Question

We've implemented the most efficient solution for this problem.

Calculate how many times the program will ask the user in the worst case scenario?

In the best case scenario, how many time will the program ask the question?
