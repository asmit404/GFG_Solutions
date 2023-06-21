'''
Title     : Reverse Coding
Author    : Asmit Singh
Solved On   : 21 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def sumOfNaturals(self, n):
        mod = 1000000007
        ans = (n * (n+1))//2
        return ans % mod

# I swear I have never seen a problem this easy on GFG. I am not even kidding.