import random

# list examples

# assignment and indexing
spam = ['item0', 'item1', 'item2']

print('item1 = ' + spam[1])
print('item2 = ' + spam[2])
print('item0 = ' + spam[0])

# list of lists
spam = [['sub_item0', 'sum_item1'], 'item1', 'item2']

print('item1 = ' + spam[1])
print('item2 = ' + spam[2])
print('sub_item1 = ' + spam[0][1])

# list sub slice and negative indexes
print('item1 = ' + spam[-2])
print('item2 = ' + spam[-1])
print('sub_item1 = ' + spam[-3][-1])

spam = ['item0', 'item1', 'item2']
print(spam)
print('1:2', spam[1:2])
print('2:', spam[2:])
print('-3:1', spam[-3:1])

# list concatenation
spam2 = ['cat', 'dog', 'pig']
print(spam)
print(spam2)
print('spam + spam2', spam + spam2)

# augmented assignment
print('spam*3', spam*3)

# del list operator
del spam[1]
print('del spam[1]', spam)

# list iteration with for loop
catNames = ['logo', 'togo', 'pogo', 'gogo']
print('for i in catNames', catNames)
for i in catNames:
    print(i)

# multi assignment
first, second = spam
print('first, second = spam: ', first, second)

spam = catNames
# list methods
print ('index of logo: ', spam.index('logo'))
spam.append('chacha')
print ('append chacha to spam: ', spam)
spam.insert(0, 'yoyo')
print ('insert "yoyo" to spam at 0: ', spam)
spam.remove('yoyo')
print ('remove "yoyo" from spam: ', spam)

# sort methods
spam.sort()
print ('spam sorted: ', spam)
spam.sort(reverse=True)
print ('spam reverse sorted: ', spam)

# magic 8ball
messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
