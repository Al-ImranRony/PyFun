# A rainbow by python

import turtle
import time
from termcolor import colored

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
for n in range(len(colors)):
    print(" " * n, end="")
    for color in reversed(colors):
        print(colored('X', color), end="")
    print()

for n in range(len(colors)):
    print(" " * (5-n), end="")
    for color in reversed(colors):
        print(colored('X', color), end="")
    print()

# Drawing with turtle
def draw():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    turtle.pensize(5)
    turtle.bgcolor('black')
    turtle.speed(1000)
    for x in range(360):
        turtle.pencolor(colors[x % len(colors)])
        turtle.pensize(x/50)
        turtle.forward(x)
        turtle.left(59)

draw()
time.sleep(5)
