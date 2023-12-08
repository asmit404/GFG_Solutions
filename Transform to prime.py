"""
Title     : Transform to prime
Author    : Asmit Singh
Solved On   : 08 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def minNumber(self, arr, n):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        sum_arr = sum(arr)
        while not is_prime(sum_arr):
            sum_arr += 1
        return sum_arr - sum(arr)

# Time Complexity  : O(N * sqrt(M))
# Space Complexity : O(1)