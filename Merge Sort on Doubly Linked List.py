'''
Title     : Merge Sort on Doubly Linked List
Author    : Asmit Singh
Solved On   : 27 Apr 2024
Solved Using   : Python3
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    def sortDoubly(self, head):
        def mergesort(node):
            if not node.next: return node
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow
            mid.prev.next = None
            mid.prev = None

            left = mergesort(node)
            right = mergesort(mid)

            dummy = Node(None)
            curr = dummy

            while left or right:
                if left and right:
                    if left.data <= right.data:
                        curr.next = left
                        left.prev = curr
                        left = left.next
                    else:
                        curr.next = right
                        right.prev = curr
                        right = right.next
                elif left:
                    curr.next = left
                    left.prev = curr
                    left = None
                elif right:
                    curr.next = right
                    right.prev = curr
                    right = None
                if curr:
                    curr = curr.next

            if dummy.next:
                dummy.next.prev = None
            return dummy.next

        return mergesort(head)

# Time Complexity: O(n log n)
# Space Complexity: O(log n)