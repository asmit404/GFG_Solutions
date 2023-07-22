"""
Title     : Remove Duplicates from an unsorted linked list
Author    : Asmit Singh
Solved On   : 22 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def removeDuplicates(self, head):
        node = head
        dupes = set()
        dupes.add(head.data)
        while node.next:
            if node.next.data in dupes:
                node.next = node.next.next
            else:
                dupes.add(node.next.data)
                node = node.next
        return head
