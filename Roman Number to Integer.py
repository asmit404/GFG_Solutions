"""
Title     : Roman Number to Integer
Author    : Asmit Singh
Solved On   : 4 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def romanToDecimal(self, S):
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        prev_value = 0
        for ch in reversed(S):
            value = dic[ch]
            ans += -value if value < prev_value else value
            prev_value = value
        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)