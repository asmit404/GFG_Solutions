'''
Title     : Remove every kth node
Author    : Asmit Singh
Solved On   : 29 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def deleteK(self, head, k):
        if k == 1: return None
        cnt, curr = 1, head
        while curr:
            if cnt == k-1 and curr.next is not None:
                curr.next = curr.next.next
                cnt = 0
            cnt, curr = cnt + 1, curr.next
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)