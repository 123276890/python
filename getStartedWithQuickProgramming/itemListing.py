# -*- coding: utf-8 -*-
# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字典。
# 其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物品。
# 例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# 意味着玩家有1 条绳索、6 个火把、42 枚金币等。

d = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(d):
    print('Inventory:')
    item_total = 0
    for k, v in d.items():
        print(k + ':' + str(v))
        item_total += v
    print('Total number of items:' + str(item_total))

# displayInventory(d)


# 写一个名为addToInventory(inventory, addedItems)的函数，其中inventory 参数是一个字典，
# 表示玩家的物品清单（像前面项目一样），addedItems 参数是一个列表，就像dragonLoot。

def addToInventory(inventory={}, addedItems=[]):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)