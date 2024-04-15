'''
Title     : Count the elements
Author    : Asmit Singh
Solved On   : 15 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def countElements(self, a, b, n, query, q):
        res = []
        count = [0] * (max(b)+1)
        for item in b:
            count[item] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        for item in query:
            ele = a[item]
            if ele > (len(count)-1):
                res.append(count[-1])
            else:
                res.append(count[ele])
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)