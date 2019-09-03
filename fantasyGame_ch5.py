import pprint

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def printInventory(inventory):
    print('Inventory: ')
    total_items = 0
    for item, num in inventory.items():
        print(str(num) + ' ' + item)
        total_items = total_items + num
    print('Total number of items: ', total_items)

    
def addToInventory(inventory, itemsToAdd):
    for i in itemsToAdd:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    printInventory(inventory)


printInventory(inventory)
addToInventory(inventory, dragonLoot)
