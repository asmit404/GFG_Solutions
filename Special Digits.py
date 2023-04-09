"""
Title     : Special Digits
Domain    : Combinatorial, Mathematical
Author    : Asmit Singh
Solved On   : 09 Apr 2023
Solved Using   : Python3
"""

MOD = 10 ** 9 + 7
def power(a, n):
    if n == 0 or a == 1:
        return 1
    if n == 1:
        return a
    x = power(a, n // 2)
    x *= x
    if n % 2:
        x *= a
    return x % MOD

def modInverse(a):
    return power(a, MOD - 2)

fac, invfac = [0] * (10 ** 5 + 1), [0] * (10 ** 5 + 1)
fac[0] = invfac[0] = 1

for i in range(1, 10 ** 5 + 1):
    fac[i] = (i * fac[i - 1]) % MOD
    invfac[i] = modInverse(fac[i])

class Solution:
    def bestNumbers(self, N: int, A: int, B: int, C: int, D: int) -> int:
        if A == B:
            p = N * A
            if str(C) in str(p) or str(D) in str(p):
                return 1
            return 0
        if A > B:
            A, B = B, A
        ans = 0
        for sum in range(A * N, B * N + 1, B - A):
            if str(C) in str(sum) or str(D) in str(sum):
                b = (sum - A * N) // (B - A)
                a = N - b
                ans += (fac[N] * invfac[a] * invfac[b]) % MOD
                ans %= MOD
        return ans
