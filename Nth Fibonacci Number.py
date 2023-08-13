"""
Title     : Nth Fibonacci Number
Author    : Asmit Singh
Solved On   : 13 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n < 2:
            return n
        MOD = 1000000007
        def multiply(A, B):
            a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
            e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
            return [[(a*e + b*g) % MOD, (a*f + b*h) % MOD], [(c*e + d*g) % MOD, (c*f + d*h) % MOD]]
        def power(A, n):
            if n == 1:
                return A
            if n % 2 == 0:
                B = power(A, n//2)
                return multiply(B, B)
            else:
                B = power(A, n-1)
                return multiply(A, B)
        A = [[1, 1], [1, 0]]
        return power(A, n-1)[0][0]

# Time Complexity : O(log n)
# Space Complexity : O(1)