'''
Title     : Find the N-th character
Author    : Asmit Singh
Solved On   : 09 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def nthCharacter(self, s, r, n):
        p = [2**i for i in range(r + 1)]
        n += 1

        def dfs(n, r, bit):
            return bit if n == 1 else dfs(n, r - 1, bit) if n <= p[r] // 2 else dfs(n - p[r] // 2, r, bit ^ 1)

        for i, bit in enumerate(s):
            if n <= p[r]:
                return dfs(n, r, int(bit))
            n -= p[r]

# Time Complexity: O(r)
# Space Complexity: O(r)