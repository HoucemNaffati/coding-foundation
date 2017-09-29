Write a small game in python
============================

Today we covered a few but very important building blocks in python
while we wrote a small game. The game suppose to pick a random
number and ask the user to guess, it tells whether the guess was
correct or the number is higher or lower than that. If the user
guess the correct number the game ends.

Write the code in plain English first
-------------------------------------

You don't have to know any programming language to be able
to write down the steps for this game, you can use plain
English.

.. code-block::

   Number = Pick a random number between 1 and 10

   Guess = -1

   while Guess is not equal to Number
       Guess = ask the user to enter a number

       if Number is lower than Guess
           Say "My number is smaller than that, try again"
       if Number is higher than Guess
           Say "My number is higher than that, try again"
       if Number is equal to Guess
           Say "Well done!"

Basically we only have to translate this code to python.

I encourage you if you ever have to solve a program with any
programming language start to design the code like this.
Don't worry if you cannot translate that just yet, but
understand how to solve an problem is the most important part
of programming.

We can play with that if we run this program in our mind:
Evaluate every line and do what it says *exactly* (not more!) and
write down the state of variables, like the following:

+-----------------------------------------------------+---------+---------+
| Action and outcome                                  |  Number | Guess   |
+=====================================================+=========+=========+
| Start the program                                   | Nothing | Nothing |
+-----------------------------------------------------+---------+---------+
| Pick the random number, let's say 5                 |         |         |
| Set to Number                                       |       5 | Nothing |
+-----------------------------------------------------+---------+---------+
| Set the Guess to -1 (initialise)                    |       5 |      -1 |
+-----------------------------------------------------+---------+---------+
| Repeat the following code                           |         |         |
| if Guess is not equal to Number. This statement is  |         |         |
| True as Guess isn't equal to Number, so we enter    |         |         |
| the loop.                                           |       5 |      -1 |
+-----------------------------------------------------+---------+---------+
| Ask user to guess a number and set Guess            |         |         |
| Let's assume user types 3                           |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is lower than Guess                |         |         |
| It is not, we don't do anything else                |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is higher than Guess               |         |         |
| It is                                               |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Print the message: "My number is higher"            |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is equal to Guess                  |         |         |
| It is not, we don't do anything else                |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Repeat the following code                           |         |         |
| if Guess is not equal to Number. This statement is  |         |         |
| *still* True as Guess isn't equal to Number,        |         |         |
| so we enter to the loop again                       |       5 |       3 |
+-----------------------------------------------------+---------+---------+
| Ask user to guess a number and set Guess            |         |         |
| Let's assume user types 5                           |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is lower than Guess                |         |         |
| It is not, we don't do anything else                |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is higher than Guess               |         |         |
| It is not, we don't do anything else                |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| Decide if Number is equal to Guess                  |         |         |
| It is                                               |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| Print the message: "Well done"                      |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| Repeat the following code                           |         |         |
| if Guess is not equal to Number. This statement is  |         |         |
| False now. We don't do anything, jump after         |         |         |
| the loop.                                           |       5 |       5 |
+-----------------------------------------------------+---------+---------+
| End of program, no more statement...                |       5 |       5 |
+-----------------------------------------------------+---------+---------+


Explanation why we set -1 to Guess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If we don't initialise the `Guess` we cannot compare it to a number.
We had to find an appropriate value for that, which will be good
enough to enter the loop.


Write the python code
---------------------

As I mentioned above, we just have to translate, but how?
We need do the following in python:
- Pick a random number
- Ask the user to enter a number
- Repeat some code
- Compare numbers and take decision based on that

For the loop I cannot give you links, since in python
you can do it in many ways and I think it's easier to
focus on one simple solution.

Pick a random number
~~~~~~~~~~~~~~~~~~~~

`Go to the official python documentation<https://docs.python.org/3/library/random.html>`

You can and should use google to find answers, nothing wrong with that.
The good googling skills are very important!

I've found the following links, and I think it could help you to understand
the python abilities to pick random numbers:
http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

An another good link: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

Usually when I want to understand something, I try to search for something like this:
`python random example`

Ask the user to enter a number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will use the built-in python function, called `input()`:

https://docs.python.org/3/library/functions.html#input


Translate to python
-------------------

Modules in python
~~~~~~~~~~~~~~~~~

If you start write a program very soon you reach the point
when you feel the code is getting disorganised, file is getting too big.
You can separate the code into multiple files and you can use
that from the others.
The other good thing of doing this is that you can use your code again
as part of different application.
The third and maybe the most important part that we can use code
written by somebody else.

Syntax the following:

.. code-block:: python

          import random
          # And we can use the random module now:
          number = random.randint(1, 10)

The code
~~~~~~~~

.. code-block:: python

          import random

          number = random.randint(1, 10)

          guess = -1

          while guess != number:
              guess = input('Guess a number: ')

              if guess > number:
                  print('My number is lower, try again')

              if guess < number:
                  print('My number is higher, try again')

              if guess == number:
                  print('Well done!')
