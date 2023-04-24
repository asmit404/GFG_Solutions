'''
Title     : Nearest Smaller Number
Domain    : ???
Author    : Asmit Singh
Solved On   : 24 Apr 2023
Solved Using   : Python3
'''

from collections import deque
class Solution:
    def nearestSmallestTower(self, arr):
        n = len(arr)
        left, right = deque(), deque()
        ans = [-1] * n
        for i in range(n):
            while left and arr[left[-1]] >= arr[i]:
                left.pop()
            if left:
                ans[i] = left[-1]
            left.append(i)
        for i in range(n-1, -1, -1):
            while right and arr[right[-1]] >= arr[i]:
                right.pop()
            if right:
                if ans[i] != -1:
                    if abs(ans[i] - i) == abs(right[-1] - i):
                        if arr[ans[i]] > arr[right[-1]]:
                            ans[i] = right[-1]
                    elif abs(ans[i] - i) > abs(right[-1] - i):
                        ans[i] = right[-1]
                else:
                    ans[i] = right[-1]
            right.append(i)
        return ans
