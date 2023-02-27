'''
Title     : Reverse Both Parts
Domain    : Linked List, Data Structures
Author    : Asmit Singh
Solved On   : 27 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        cur = head
        res = Node(0)
        while k > 0:
            t, cur = cur, cur.next
            res.next, t.next = t, res.next
            k -= 1
        while cur:
            t, cur = cur, cur.next
            head.next, t.next = t, head.next
        return res.next
