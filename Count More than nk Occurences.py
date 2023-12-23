"""
Title     : Count More than n/k Occurences
Author    : Asmit Singh
Solved On   : 23 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countOccurence(self, arr, n, k):
        cnt = {}
        for num in arr:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        return sum(1 for val in cnt.values() if val > n//k)

# Time Complexity  : O(n)
# Space Complexity : O(n)