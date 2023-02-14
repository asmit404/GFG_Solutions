'''
Title     : Walls Coloring
Domain    : Dynamic Programming
Author    : Asmit Singh
Solved On   : 14 Feb 2023
Solved Using   : Python3

'''

class Solution():
    def minCost(self, color, N):
        for i in range(1,N):
            color[i][0]+=min(color[i-1][1],color[i-1][2])
            color[i][1]+=min(color[i-1][2],color[i-1][0])
            color[i][2]+=min(color[i-1][1],color[i-1][0])
        return min(color[-1]) 
