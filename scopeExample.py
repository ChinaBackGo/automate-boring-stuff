#scope example

global_var = 'This CAN be used outside any function'

def scopeExample():
    print(global_var)
    local_var = 'This cant be used outside this function'
    print(local_var)
local_var = 'This is not a local var'
scopeExample()
print(local_var)

def spam():
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    # prints 'bacon local'
    print(eggs)
    spam()
    # prints 'bacon local'
    print(eggs)

eggs = 'global'
bacon()
# prints 'global'
print(eggs)



 
