"""
Title     : Recamans sequence
Author    : Asmit Singh
Solved On   : 11 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def recamanSequence(self, n):
        seq = [0] * n
        seen = set()
        seen.add(0)
        for i in range(1, n):
            nxt = seq[i-1] - i
            if nxt > 0 and nxt not in seen:
                seq[i] = nxt
                seen.add(nxt)
            else:
                seq[i] = seq[i-1] + i
                seen.add(seq[i])
        return seq

# Time Complexity: O(n)
# Space Complexity: O(n)