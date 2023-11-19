"""
Title     : Intersection of two sorted Linked lists
Author    : Asmit Singh
Solved On   : 19 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def findIntersection(self,head1,head2):
        tmp = res = Node(0)
        while head1 and head2:
            if head1.data < head2.data:
                head1 = head1.next
            elif head1.data > head2.data:
                head2 = head2.next
            else:
                res.next = head1
                res = res.next
                head1 = head1.next
                head2 = head2.next
        res.next = None
        return tmp.next

# Time Complexity : O(n)
# Space Complexity : O(1)