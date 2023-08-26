"""
Title     : Longest K unique characters substring
Author    : Asmit Singh
Solved On   : 26 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def longestKSubstr(self, s, k):
        i, max_len, count = 0, -1, {}
        for j in range(len(s)):
            count.setdefault(s[j], 0)
            count[s[j]] += 1
            while len(count) > k:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    count.pop(s[i])
                i += 1
            if len(count) == k:
                max_len = max(max_len, j - i + 1)
        return max_len

# Time Complexity: O(N)
# Space Complexity: O(K)