"""
Title     : Reverse a Doubly Linked List
Author    : Asmit Singh
Solved On   : 18 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def reverseDLL(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        return prev

# Time Complexity : O(n)
# Space Complexity : O(1)