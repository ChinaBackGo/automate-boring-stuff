import random

guess = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20')
print('answer: ', guess)

user_guess = 0
num_guess = 0
while guess != user_guess:
    print('Take a guess')
    user_guess = int(input())
    num_guess += 1
    if guess < user_guess:
        print('Too high')
    if guess > user_guess:
        print('Too low')
print ('That\'s right!')
print ('You took: ' + str(num_guess) + ' guesses!')
