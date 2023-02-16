'''
Title     : Good Stones
Domain    : Greedy, Dynamic Programming, Graph
Author    : Asmit Singh
Solved On   : 16 Feb 2023
Solved Using   : Python3
'''
   
class Solution:
    def goodStones(self, n, arr) -> int:
        visited=[0]*n
        def solve(i):
            nonlocal arr,visited,n
            if i<0 or i>=n:
                return True
            if visited[i]>0:
                return visited[i]==2
            visited[i]=1
            if solve(i+arr[i]):
                visited[i]=2
                return True
            return False
        return sum(solve(i) for i in range(n))
