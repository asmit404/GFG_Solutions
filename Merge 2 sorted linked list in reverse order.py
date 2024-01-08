"""
Title     : Merge 2 sorted linked list in reverse order
Author    : Asmit Singh
Solved On   : 8 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def mergeResult(self, h1, h2):
        if not h1 or not h2: return self.reverse_list(h1 or h2)
        res, h1, h2 = (h1, h1.next, h2) if h1.data <= h2.data else (h2, h1, h2.next)

        curr = res
        while h1 and h2:
            curr.next, h1, h2 = (
                h1, h1.next, h2) if h1.data <= h2.data else (h2, h1, h2.next)
            curr = curr.next

        curr.next = h1 or h2
        return self.reverse_list(res)

# Time Complexity : O(n + m)
# Space Complexity : O(1)