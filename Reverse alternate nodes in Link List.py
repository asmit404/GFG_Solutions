"""
Title     : Reverse alternate nodes in Link List
Author    : Asmit Singh
Solved On   : 6 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def rearrange(self, odd):
        olist, elist = [], []
        curr = odd
        while curr is not None:
            olist.append(curr.data)
            curr = curr.next
            if curr is not None:
                elist.append(curr.data)
                curr = curr.next
        elist.reverse()
        olist.extend(elist)
        curr = odd
        i = 0
        while curr is not None:
            curr.data = olist[i]
            i += 1
            curr = curr.next
        return

# Time Complexity: O(n)
# Space Complexity: O(n)