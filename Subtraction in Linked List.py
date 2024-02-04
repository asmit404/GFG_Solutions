"""
Title     : Subtraction in Linked List
Author    : Asmit Singh
Solved On   : 04 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def subLinkedList(self, l1, l2):
        def compute(head):
            var, curr = 0, head
            while curr:
                var = var * 10 + curr.data
                curr = curr.next
            return var

        a1, a2 = compute(l1), compute(l2)
        return Node(abs(a1-a2))

# Time Complexity: O(n)
# Space Complexity: O(n)