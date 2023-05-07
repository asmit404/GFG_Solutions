'''
Title     : String Mirror
Author    : Asmit Singh
Solved On   : 7 May 2023
Solved Using   : Python3
'''

class Solution:
    def stringMirror(self, str: str) -> str:
        s = str[0]
        for i in range(1, len(str)):
            if ord(s[-1]) > ord(str[i]) or (ord(s[-1]) >= ord(str[i]) and i > 1):
                s += str[i]
            else:
                break
        return s+s[::-1]
