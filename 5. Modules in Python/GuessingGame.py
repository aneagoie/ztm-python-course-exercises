import sys

from random import randint

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(
            input('Please choose a number that falls between those two you just chose: '))
        if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
    except ValueError:
        print("Please enter a number")
        continue