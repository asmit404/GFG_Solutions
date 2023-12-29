"""
Title     : Check if a string is repetition of its substring of k-length
Author    : Asmit Singh
Solved On   : 29 Dec 2023
Solved Using   : Python3
"""

from collections import Counter
class Solution:
    def kSubstrConcat(self, n, s, k):
        if n % k != 0: return 0
        substr = [s[i:i+k] for i in range(0, n, k)]
        cnt = Counter(substr)
        maxi = max(cnt.values())
        return 0 if maxi < (n/k) - 1 else 1

# Time Complexity  : O(n)
# Space Complexity : O(n)