"""
Title     : Level order traversal in spiral form
Author    : Asmit Singh
Solved On   : 25 Jul 2023
Solved Using   : Python3
"""

def findSpiral(root):
    res, st, k = [], [root], -1
    while len(st) > 0:
        pool, temp = [], []
        for i in st:
            if i == None:
                continue
            temp.append(i.left)
            temp.append(i.right)
            pool.append(i.data)
        st = temp[:]
        res = res + pool[::k]
        k *= -1
    return res
