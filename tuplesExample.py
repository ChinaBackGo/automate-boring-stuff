# tuples examples
print('tuple example 1:')

eggs = ('hello', 42, 0.5)
print('eggs = \'hello\', 42, 0.5')
print('eggs[0]')
print(eggs[0])

print('tuple and list conversion example 2:')
eggs_list = ['hello', 42, 0.5]

print('tuple(eggs_list)')
print(tuple(eggs_list))

print('list(eggs)')
print(list(eggs))


print('lists are references example')
list_ref = [1,2,3]
list_ref2 = list_ref

print('list_ref = [1,2,3')
print('list_ref2 = list_ref')

del list_ref[1]
print ('del list_ref[1]')

print(list_ref)
print(list_ref2)

import copy

print('list_ref2 = copy.copy(list_ref)')
print('list_ref2.append(2)')

# note, lists that contain lists use deepcopy()
list_ref2 = copy.copy(list_ref)
list_ref2.append(2)

print(list_ref)
print(list_ref2)
