import pprint
# myCat dictionary examples
myCat = {'size': 'fat', 'colour':'grey', 'disposition':'loud'}
print("myCat = {'size': 'fat', 'colour':'grey', 'disposition':'loud'}")
print(myCat)

print("print(myCat['size'])")
print(myCat['size'])

print('myCat.values, myCat.keys, myCat.items')


# how to iterate with values, keys, items Dict methods
for v in myCat.values():
    print(v)

for k in myCat.keys():
    print(k)

for i in myCat.items():
    print(i)

for k, v in myCat.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Testing whether key exists
# without values()/keys() defaults to value

print('fat value exist in myCat?', 'fat' in myCat.values())

# get() method
print('I have a ' + str(myCat.get('size', 'skinny')) + ' cat.')

# setDefault()

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
