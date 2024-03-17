'''
Title     : Count Pairs whose sum is equal to X
Author    : Asmit Singh
Solved On   : 17 Mar 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        res, cnt = {}, 0
        while head1:
            res[head1.data] = res.get(head1.data, 0)+1
            head1 = head1.next
        while head2:
            if x-head2.data in res:
                cnt += res[x-head2.data]
            head2 = head2.next
        return cnt

# Time Complexity: O(n1 + n2)
# Space Complexity: O(n1)