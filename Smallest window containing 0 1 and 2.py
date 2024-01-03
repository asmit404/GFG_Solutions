"""
Title     : Smallest window containing 0, 1 and 2
Author    : Asmit Singh
Solved On   : 3 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def smallestSubstring(self, S):
        indices = {}
        minLength = float('inf')

        for i, char in enumerate(S):
            indices[char] = i

            if '0' in indices and '1' in indices and '2' in indices:
                minLength = min(minLength, 1 + i - min(indices.values()))

        return minLength if len(indices) == 3 else -1

# Time Complexity  : O(n)
# Space Complexity : O(1)