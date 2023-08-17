"""
Title     : Next Smallest Palindrome
Author    : Asmit Singh
Solved On   : 17 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def generateNextPalindrome(self, num, n):
        if all(num[i] == 9 for i in range(n)):
            return [1] + [0] * (n-1) + [1]

        pal = num[:]
        pal[(n+1)//2:] = (pal[:n//2])[::-1]
        if pal > num:
            return pal

        for i in range((n-1)//2, -1, -1):
            if num[i] < 9:
                num[i] += 1
                break
            num[i] = 0

        num[(n+1)//2:] = (num[:n//2])[::-1]
        return num

# Time Complexity: O(n)
# Space Complexity: O(n)