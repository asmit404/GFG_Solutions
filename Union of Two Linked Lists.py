'''
Title     : Union of Two Linked Lists
Author    : Asmit Singh
Solved On   : 27 Jun 2023
Solved Using   : Python3
'''

from bisect import *
class Solution:
    def union(self, head1, head2):
        pool = set()
        temp1 = head1
        temp2 = head2
        while temp1:
            pool.add(temp1.data)
            temp1 = temp1.next
        while temp2:
            pool.add(temp2.data)
            temp2 = temp2.next
        pool = list(sorted(pool))
        res = Node(pool[0])
        temp = res
        for i in range(1, len(pool)):
            ans = Node(pool[i])
            temp.next = ans
            temp = temp.next
        return res
