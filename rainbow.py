# A rainbow by python

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