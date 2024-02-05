"""
Title     : Sorted insert for circular linked list
Author    : Asmit Singh
Solved On   : 05 Feb 2024
Solved Using   : Python3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        nn = Node(data)
        if not head:
            nn.next = nn
            return nn
        curr = head

        if data < head.data:
            while curr.next != head:
                curr = curr.next
            curr.next = nn
            nn.next = head
            return nn

        while curr.next != head and curr.next.data < data:
            curr = curr.next
        nn.next = curr.next
        curr.next = nn
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)