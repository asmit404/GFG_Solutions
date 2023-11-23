"""
Title     : AVL Tree Insertion
Author    : Asmit Singh
Solved On   : 23 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def getHeight(self, root):
        if root is None: return 0
        return root.height

    def getBalance(self, root):
        if root is None: return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, root):
        y = root.right
        t2 = y.left
        root.right = t2
        y.left = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, root):
        y = root.left
        t2 = y.right
        root.left = t2
        y.right = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insertToAVL(self, root, key):
        if root is None: return Node(key)
        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        elif key > root.data:
            root.right = self.insertToAVL(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if key > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

# Time Complexity : O(log n)
# Space Complexity : O(h)