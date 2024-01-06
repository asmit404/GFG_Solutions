"""
Title     : Techfest and the Queue
Author    : Asmit Singh
Solved On   : 6 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def sumOfPowers(self, a: int, b: int) -> int:
        pool, cnt = list(range(b + 1)), 0
        for i in range(2, int(b ** 0.5) + 1):
            if pool[i] == i:
                for j in range(i * i, b + 1, i):
                    if pool[j] == j:
                        pool[j] = i
        for num in range(a, b + 1):
            while num > 1:
                div = pool[num]
                while num % div == 0:
                    cnt += 1
                    num //= div
        return cnt

# Time Complexity : O(n log log n + m log n)?
# Space Complexity : O(n)