'''
Title     : Search Pattern (Rabin-Karp Algorithm)
Author    : Asmit Singh
Solved On   : 06 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def search(self, pattern, text):
        pool = []
        n = len(pattern)
        for i in range(len(text) - n + 1):
            if text[i:i + n] == pattern:
                pool.append(i + 1)
        return pool

# I have no fucking idea what is this time and space complexity.
# Time Complexity: O((m - n + 1) * n)
# Space Complexity: O(m)