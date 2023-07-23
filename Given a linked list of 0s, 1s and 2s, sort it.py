"""
Title     : Given a linked list of 0s, 1s and 2s, sort it
Author    : Asmit Singh
Solved On   : 23 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def segregate(self, head):
        pool = []
        curr_node = head

        while curr_node:
            pool.append(curr_node.data)
            curr_node = curr_node.next

        pool.sort()
        ll = LinkedList()
        for i in pool:
            ll.append(i)
        return ll.head
