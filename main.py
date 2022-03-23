# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
from typing import List

scret = 9
guess_count = 0
guess_limit = 3
while   guess_count < guess_limit:
    Guess = int(input('what is the guess:'))
    guess_count += 1
    if Guess == scret:
        print("you won")
        break
    print("make another guess")
else:
    print("you lose")













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
