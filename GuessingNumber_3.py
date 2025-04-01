# Generate a random integer between 1 to 100 import random
import random
jackpot = random.randint(1,100)

guess = int(input('Enter a number: '))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('Wrong! number is greater')
    else:
        print('wrong ! Number is Lower')
    guess = int(input("Enter again: "))
    counter += 1
else:
    print('Congratulation ! You Guess it')
    print('Number of attemps: ',counter)