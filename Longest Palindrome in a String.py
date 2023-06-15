'''
Title     : Longest Palindrome in a String
Author    : Asmit Singh
Solved On   : 15 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def longestPalin(self, s):
        if len(s) == 1:
            return s
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                x = s[j:i+j]
                if x == x[::-1]:
                    return x
