First steps in the python world
===============================

In this session we installed the python to our local computers,
and tried different basic commands to execute.

Choose of language
------------------

We started to learn python a bit. My main objective for the first few
session is to make you interested and understand some concepts.
I've decided to introduce `python <https://www.python.org>` first.
Not just because at `made.com <https://made.com/>` we use that, mainly
for our backoffice services, but I believe that's a very good first language
to learn. The introduced concepts can be applied mainly on any language.


First python tutorial
---------------------

One of the tutorials that we plan to go through together:
https://cscircles.cemc.uwaterloo.ca/

To be able to complete this tutorial you don't need to install anything
locally.


Install anaconda
----------------

As we learn things through the tutorial it's worth to try them locally as well.
Although, installing python in everyone's computer can be a difficult task for me.
Python is supposed to function the same way (in most cases) in any operating system,
but the tools around python, installing dependences (I'll cover it later),
can be very difficult.

We'll use `Anaconda <https://www.anaconda.com>` to manage python packages.
This is a very popular choice amongst Data Scientists, who want to focus
in building the scripts and accomplish tasks using python.

It comes with many tools like:
- `Anaconda Navigator <https://docs.anaconda.com/anaconda/navigator/>`
- `Spyder <https://pythonhosted.org/spyder/>` as a powerful code editor.
- `jupyter <http://jupyter.readthedocs.io/en/latest/>` which is python console through web

Hello World
-----------

We wrote together one of the most common programs, which is well known amongst every programmer
in every level, the `Hello World` program.

The code is only `print("Hello World")`. It only prints "Hello World" in the screen,
although this also serves an important purpose, to tell us that our setup works well.

Strings
-------

In this first session we've understood (if not, please let me know!!!) what is a string.
A string is basically sequence of characters. We can use `'`, `"` (single and double quotes)
to write one.
The string is a very commonly used type in most modern Programming Languages.

I've showed how to concatenate strings (join them) together: `"first name" + " " + 'last name'`.

Numbers
-------

Python works well with numbers as well. It understands `3 + 4` statements as well.

We've tried to concatenate numbers and strings, and we saw a rather ugly error message:

>>> "hello" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>>>

Variables
---------

The next thing I've shown you, is how to use variables.
Variables represent reserved memory blocks that we can access using a label, the name of the variable.
I've shown how can you assign values to variable, and how can you reassign new values.

>>> first_name = "Csaba"
>>> last_name = "Palankai"
>>> print(first_name, last_name)
Csaba Palankai

We can use a 3rd variable to keep their concatenated value:

>>> full_name = first_name + ' ' + last_name
>>> print(full_name)
Csaba Palankai


We can reassign the values of existing variables:
>>> first_name = 'Gitta'
>>> print(full_name)
Csaba Palankai

Surprise, you may expect to see my my sister's name, although,
we have to set the value of `full_name` again in order to do that.

>>> full_name = first_name + ' ' + last_name
>>> print(full_name)
Gitta Palankai


A real problem
--------------

I had a real problem a few days ago. I wanted to have some water for my
coffee which is around 80°C. Although I only have boiling water or 20°C.
I've decided to mix them to achieve my goal.

I used a small python script:

>>> amount_boiling = 1
>>> temp_boiling = 100
>>> amount_cold = 0.3
>>> temp_cold = 20
>>> (amount_boiling * temp_boiling + amount_cold * temp_cold) / (amount_boiling + amount_cold)
81.53846153846153

You can see how easy is to use python to calculate something useful.

Functions
---------

Let's imagine you have to do similar calculations very often.
But as a programmer you will make mistakes (which is perfectly normal), but you can
avoid them. You have to avoid repeating yourself.

>>> def calculate_mixed_water_temperature(added_water_amount):
...     amount_boiling = 1
...     temp_boiling = 100
...     amount_cold = added_water_amount
...     temp_cold = 20
...     return (amount_boiling * temp_boiling + amount_cold * temp_cold) / (amount_boiling + amount_cold)
...
>>> calculate_mixed_water_temperature(.3)
81.53846153846153
>>> calculate_mixed_water_temperature(.3)
81.53846153846153
>>> calculate_mixed_water_temperature(.2)
86.66666666666667
>>> calculate_mixed_water_temperature(.4)
77.14285714285715

As you can see we can easily reuse the written function.
We can easily try it with different values.

Reading of the traceback, understanding errors
----------------------------------------------

>>> def calculate_mixed_water_temperature(added_water_amount):
...     amount_boiling = 1
...     temp_boiling = 100
...     amount_cold = added_water_amount
...     temp_cold = 20
...     return (amount_boiling * temp_boiling + amount_cold * temp_cold) / (unknown_variable + amount_cold)
...
>>> calculate_mixed_water_temperature(.4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in calculate_mixed_water_temperature
NameError: name 'unknown_variable' is not defined

I've intentionally replaced one variable in the code. And python doesn't like me anymore.
I encourage you to copy the error message `NameError: name 'unknown_variable' is not defined`
and try to search on google (or any preferred search engine).
Although, in this case it's easy to understand the error.
The traceback says the line numbers, so you can easily find the error.

Questions
---------

How can you remember the name/meaning of a variable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is no easy way to remember them. It's only a best practice but
you can use long(er) variable names, so when you read a code weeks later,
or use the variable somewhere else you can read that.

Why I type many spaces around symbols?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spaces are just there to help us read the code. Both of the following statements work the same way:

>>> (amount_boiling * temp_boiling + amount_cold * temp_cold) / (amount_boiling + amount_cold)
81.53846153846153

>>> (amount_boiling*temp_boiling+amount_cold*temp_cold) /      (amount_boiling+   amount_cold)
81.53846153846153
