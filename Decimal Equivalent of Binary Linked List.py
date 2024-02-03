"""
Title     : Decimal Equivalent of Binary Linked List
Author    : Asmit Singh
Solved On   : 03 Feb 2024
Solved Using   : Python3
"""

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    def decimalValue(self, head):
        MOD = 1000000007
        num = 0
        while head:
            num = ((num << 1) | head.data) % MOD
            head = head.next
        return num

# Time Complexity: O(n)
# Space Complexity: O(1)