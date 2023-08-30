"""
Title     : Delete a node in Single Linked List
Author    : Asmit Singh
Solved On   : 30 Aug 2023
Solved Using   : Python3
"""

def delNode(head, k):
    if not head:
        return None
    if k == 1:
        return head.next
    temp = head
    while temp.next:
        if k == 2:
            temp.next = temp.next.next
            break
        k -= 1
        temp = temp.next
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)