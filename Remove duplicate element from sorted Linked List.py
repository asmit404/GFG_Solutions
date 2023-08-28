"""
Title     : Remove duplicate element from sorted Linked List
Author    : Asmit Singh
Solved On   : 28 Aug 2023
Solved Using   : Python3
"""

def removeDuplicates(head):
    if head is None:
        return None
    curr = head
    while curr is not None:
        lmao = curr.next
        while lmao is not None and lmao.data == curr.data:
            lmao = lmao.next
        curr.next = lmao
        curr = curr.next
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)