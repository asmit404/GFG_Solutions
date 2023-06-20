'''
Title     : Matchsticks game
Author    : Asmit Singh
Solved On   : 20 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def matchGame(self, N):
        return N % 5 if N % 5 != 0 else -1

# This is possibly the simplest problem I have ever solved on GFG.