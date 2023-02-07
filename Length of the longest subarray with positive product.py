'''
Title     : Length of the longest subarray with positive product
Domain    : Dynamic Programming, Algorithms
Author    : Asmit Singh
Solved On   : 07 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def maxLength(self,arr,n):
        pos_len, neg_len, ans = 0, 0, 0
        for e in arr:
            if e == 0:
                pos_len = neg_len = 0
            elif e < 0:
                pos_len, neg_len = neg_len+1 if neg_len else 0, pos_len+1
            else:
                neg_len, pos_len = neg_len+1 if neg_len else 0, pos_len+1
            ans = max(ans, pos_len)
        return ans
