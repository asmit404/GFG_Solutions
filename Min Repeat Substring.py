'''
Title     : Minimum times A has to be repeated such that B is a substring of it
Domain    : Searching, Strings, Pattern Searching, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 31 Jan 2023
Solved Using   : Python3
'''

class Solution: 
    def issubstring(self, str2, rep):
        if str2 in rep:
            return True
        return False
    
    def minRepeats(self, A, B):
        ans = 1
        S = A
        
        while len(S)<len(B):
            S += A 
            ans += 1 
            
        if self.issubstring(B,S):
            return ans 
        elif self.issubstring(B,S+A):
            return ans+1 
        else:
            return -1
