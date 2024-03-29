'''
Title     : Median of the Subarrays
Domain    : Sorting, Map, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 18 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def countSubarray(self, N, A, M):
        def fn(n, A, m):
            mp = [0]*(2*n+1)
            cur, tot, ans = n, 0, 0
            mp[cur] += 1
            for i in range(n):
                x = -1
                if (A[i] >= m):
                    x = 1
                if (x == -1):
                    tot -= mp[(cur+x)]
                else:
                    tot += mp[cur]
                cur += x
                ans += tot
                mp[cur] += 1
            return ans
        return fn(N, A, M) - fn(N, A, M+1)
