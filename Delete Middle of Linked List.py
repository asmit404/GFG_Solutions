'''
Title     : Delete Middle of Linked List
Author    : Asmit Singh
Solved On   : 28 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def deleteMid(self, head):
        if head is None or head.next is None: return None
        slow = fast = head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if prev is not None:
            prev.next = slow.next

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)