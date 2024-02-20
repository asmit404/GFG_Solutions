"""
Title     : Word Break
Author    : Asmit Singh
Solved On   : 20 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def wordBreak(self, n, s, dictionary):
        word_set = set(dictionary)
        cache = {}
        def compute(s):
            if not s: return True
            if s in cache: return cache[s]
            for i in range(len(s), 0, -1):
                if s[:i] in word_set and compute(s[i:]):
                    cache[s] = True
                    return True
            cache[s] = False
            return False
        return compute(s)

# Time Complexity: O(n ^ 3)?
# Space Complexity: O(n)