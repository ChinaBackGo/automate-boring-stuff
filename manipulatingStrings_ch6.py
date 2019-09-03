# escape characters
print('Say hi to Bob\'s mother. with \n a tab \tab \" \\')

# raw string ignores backslash
print(r'this ignores \ ')

# multiline strings
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

# multiline comments
""" this is a multiline
comment
"""

# strings can be manipulated like lists
spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])

# string in, not in
print('hello' in 'hello there!')
print('hello' not in 'hello there!')


# useful string methods upper, lower, isupper, islower
print(spam.upper())

# chaining together
print('Hello'.upper().lower().upper())

# .startswith, .endswith
print('Hello'.startswith('H'))

# .join and .split
print(', '.join(['cats', 'rats', 'bats']))

print('My name is Simon'.split())

spam = '''Dear Alice,
How have you been? I am fine. There is a container in the fridge that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# ljust, rjust, center
print('Hello'.rjust(10))
print('>Hello'.rjust(10, '='))
print('Hello'.center(15, '*'))

# strip, lstrip, rstrip

spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
