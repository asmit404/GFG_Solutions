'''
Title     : Min Operations
Domain    : ???
Author    : Asmit Singh
Solved On   : 29 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def solve(self, a : int, b : int) -> int:
        r=a&b
        if (a==b):
            return 0
        elif (r==a or r==b):
            return 1
        else:
            return 2
