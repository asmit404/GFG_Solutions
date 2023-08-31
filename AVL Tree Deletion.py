"""
Title     : AVL Tree Deletion
Author    : Asmit Singh
Solved On   : 31 Aug 2023
Solved Using   : Python3
"""

def getHeight(node):
    if node is None:
        return 0
    return node.height

def getBalance(node):
    if node is None:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(getHeight(x.left), getHeight(x.right)) + 1
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1

    return y

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Time Complexity : O(log n)
# Space Complexity : O(log n)