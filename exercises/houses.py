from turtle import (
    done, color, setheading, up, goto, down, right, left, forward, pensize, delay
)


RIGHT_ANGLE = 90
ACUTE_ANGLE = 120
ANGLE = ACUTE_ANGLE - RIGHT_ANGLE

delay(1)
color('black', 'white')
pensize(10)


def draw_triangle(z):
    # Right ceiling
    left(ACUTE_ANGLE)
    forward(z)

    # Left ceiling
    left(ACUTE_ANGLE)
    forward(z)


def draw_square(z):
    right(RIGHT_ANGLE)
    forward(z)

    left(RIGHT_ANGLE)
    forward(z)

    left(RIGHT_ANGLE)
    forward(z)

    left(RIGHT_ANGLE)
    forward(z)


def reset(x, y):
    setheading(0)
    up()
    goto(x, y)
    down()


def house(x, y, z):
    # House
    reset(x, y)
    draw_square(z)

    # Roof
    reset(x + z, y)
    draw_triangle(z)

    # windows
    reset(x + (z / 2), y - (z / 4))
    draw_square(z / 4)
    reset(x + (z / 6), y - (z / 4))
    draw_square(z / 4)

    # Door
    reset(x + (z / 6), y - z + (z / 4))
    draw_square(z / 4)


house(-100, 100, 600)
done()
