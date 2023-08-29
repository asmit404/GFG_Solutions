"""
Title     : Delete nodes having greater value on right
Author    : Asmit Singh
Solved On   : 29 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def compute(self, head):
        curr = head
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        head = prev
        curr = head

        while curr and curr.next:
            while curr.next and curr.next.data < curr.data:
                curr.next = curr.next.next
            if curr.next:
                curr = curr.next

        curr = head
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

# Time Complexity : O(n^2)
# Space Complexity : O(1)