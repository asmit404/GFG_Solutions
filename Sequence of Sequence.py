"""
Title     : Sequence of Sequence
Author    : Asmit Singh
Solved On   : 16 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def numberSequence(self, m: int, n: int) -> int:
        return 0 if m < n else 1 if n == 0 else self.numberSequence(m // 2, n - 1) + self.numberSequence(m - 1, n)

# Time Complexity: O(2 ^ (m + n))
# Space Complexity: O(m + n)