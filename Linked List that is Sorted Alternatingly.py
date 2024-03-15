'''
Title     : Linked List that is Sorted Alternatingly
Author    : Asmit Singh
Solved On   : 15 Mar 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, h1):
        pool = []
        while h1:
            pool.append(h1.data)
            h1 = h1.next
        pool.sort()
        head = tail = Node(pool[0]) if pool else None
        for value in pool[1:]:
            if tail is not None:
                tail.next = Node(value)
                tail = tail.next
        return head

# Time Complexity: O(n log n)
# Space Complexity: O(n)