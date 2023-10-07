"""
Title     : Pairwise swap elements of a linked list
Author    : Asmit Singh
Solved On   : 7 Oct 2023
Solved Using   : Python3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def pairWiseSwap(self, head):
        dummy = Node(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            prev.next = head.next
            head.next = prev.next.next
            prev.next.next = head

            prev = head
            head = head.next

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)