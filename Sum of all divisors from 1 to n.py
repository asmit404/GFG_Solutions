"""
Title     : Sum of all divisors from 1 to n
Author    : Asmit Singh
Solved On   : 21 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def sumOfDivisors(self, N):
        return sum(i*(N//i) for i in range(1, N+1))

# Time Complexity: O(N log N)
# Space Complexity: O(1)