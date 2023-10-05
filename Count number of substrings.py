"""
Title     : Count number of substrings
Author    : Asmit Singh
Solved On   : 5 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def atMostK(self, s, k):
        if k < 0:
            return 0

        i = cnt = res = 0
        m = [0] * 26

        for j in range(len(s)):
            m[ord(s[j]) - ord('a')] += 1
            cnt += m[ord(s[j]) - ord('a')] == 1

            while cnt > k:
                m[ord(s[i]) - ord('a')] -= 1
                cnt -= m[ord(s[i]) - ord('a')] == 0
                i += 1

            res += j - i + 1

        return res

    def substrCount(self, s, k):
        return self.atMostK(s, k) - self.atMostK(s, k-1)

# Time Complexity : O(n)
# Space Complexity : O(1)