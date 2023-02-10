'''
Title     : Balloon Everywhere
Domain    : Map, Data Structures
Author    : Asmit Singh
Solved On   : 10 Feb 2023
Solved Using   : Python3
'''

from collections import Counter
class Solution:
    def maxInstance(self, s : str) -> int:
        a=Counter('balloon')
        b=Counter(s)
        mini=1e9
        for i in a:
            if i in b:
                mini=min(mini,b[i]//a[i])
            else:
                return 0
        return mini
