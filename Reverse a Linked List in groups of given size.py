"""
Title     : Reverse a Linked List in groups of given size
Author    : Asmit Singh
Solved On   : 21 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def reverse(self, head, k):
        if head == None:
            return None

        prev, next = None, None
        curr, count = head, 0

        while curr != None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next != None:
            head.next = self.reverse(next, k)
        return prev
