"""
Title     : Insert in a Sorted List
Author    : Asmit Singh
Solved On   : 8 Oct 2023
Solved Using   : Python3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head1, key):
        var = Node(key)
        if var.data < head1.data:
            var.next, head1 = head1, var
            return head1

        curr = head1
        while curr.next and var.data > curr.next.data:
            curr = curr.next

        var.next, curr.next = curr.next, var
        return head1

# Time Complexity: O(n)
# Space Complexity: O(1)