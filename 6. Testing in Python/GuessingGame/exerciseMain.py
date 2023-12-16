from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
while True:
    try:
        guess = int(input('guess a number 1~10:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue