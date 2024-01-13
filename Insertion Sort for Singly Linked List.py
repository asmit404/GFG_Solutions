"""
Title     : Insertion Sort for Singly Linked List
Author    : Asmit Singh
Solved On   : 13 Jan 2024
Solved Using   : Python3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertionSort(self, head):
        if not head or not head.next: return head
        sorted_head = Node(float('-inf'))
        sorted_head.next = head
        current = head.next
        sorted_head.next.next = None

        while current:
            next_node = current.next
            current.next = None
            curr_sorted = sorted_head

            while curr_sorted.next and curr_sorted.next.data < current.data:
                curr_sorted = curr_sorted.next

            current.next = curr_sorted.next
            curr_sorted.next = current
            current = next_node

        return sorted_head.next

# Time Complexity : O(n^2)
# Space Complexity : O(1)