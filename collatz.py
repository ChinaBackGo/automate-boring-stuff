def collatz (number):
    print ('seq: ' + str(number))
    if (number == 1):
        return
    if ((number) % 2 == 0):
        collatz(number // 2)
    else:
        collatz(3*number + 1)

print('Please input a number for collatz sequence: ')
try:
    number = int(input())
except ValueError:
    print('Please enter an interger value')
    exit()

collatz(number)
