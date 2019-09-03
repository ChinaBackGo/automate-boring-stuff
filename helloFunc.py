#functions
def hello(name):
    print('Hello ' + name)
hello('ronno')
hello('apjii')

#Functions
print('Enter a number between 1 and 10 (outside this range to exit)')

def magic8ball(answer):
    if answer == '0':
        print('it is so')
    elif answer == '1':
        print(' it is very much so ')
    elif answer == '2':
        print('it is very much soso')
    elif answer == '3':
        print('it is very much sososo')
    elif answer == '4':
        print('it is very much sosososo')
    elif answer == '5':
        print('it is very much sososososos')
    elif answer == '6':
        print('it is very much sososososososo')
    elif answer == '7':
        print('it is very much sososososososososo')
    elif answer == '8':
        print('it is very much sosososososososososo')
    elif answer == '9':
        print('it is very much sosssosososososososososo')
    else :
        print('that\'s not a valid number')
        return(False)
    return(True)
while True:
    if not magic8ball(input()):
        break

#functions without a return value return None
if print('Hi') == None:
    print('hello again')

#Keywords and arguments
print('Hello')
print('World')

print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep='::')
