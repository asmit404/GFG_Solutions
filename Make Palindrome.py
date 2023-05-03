'''
Title     : Make Palindrome
Author    : Asmit Singh
Solved On   : 3 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def makePalindrome(self, n: int, arr: List[str]) -> bool:
        res = set()
        for i in arr:
            rev = i[::-1]
            if rev in res:
                res.remove(rev)
            else:
                res.add(i)

        if len(res) > 1:
            return False
        if len(res) == 1:
            val = list(res)[0]
            return val == val[::-1]
        return True
