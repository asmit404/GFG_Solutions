'''
Title     : Smallest Positive missing number
Author    : Asmit Singh
Solved On   : 9 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def missingNumber(self,arr,n):
        arr.sort()
        res=1
        for i in range(n):
            if (arr[i]>0 and arr[i]==res):
                res+=1
        return res
