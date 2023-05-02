'''
Title     : Cake Distribution Problem
Author    : Asmit Singh
Solved On   : 2 May 2023
Solved Using   : Python3
'''

class Solution():
    def maxSweetness(self, sweetness, n, k):
        low, ans = 0, 0
        high = 1e15
        while low <= high:
            mid = (low+high)//2
            curSum, pieces = 0, 0
            for i in sweetness:
                curSum = curSum + i
                if curSum >= mid:
                    curSum = 0
                    pieces = pieces+1
            if pieces >= k+1:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return int(ans)
