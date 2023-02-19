'''
Title     : Apple Sequences
Domain    : Two Pointer Algorithm, Implementation, Algorithms
Author    : Asmit Singh
Solved On   : 18 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def appleSequences(self, n, m, arr):
        i , j = 0 , 0
        counta = 0
        counto = 0
        ans = 0
        while(j<n):
            if(arr[j] == "A"):
                counta += 1
            elif(counto < m):
                counto += 1
            else:
                while( i<j and arr[i] != "O"):
                    i += 1
                    counta -= 1
                i += 1
            ans = max(ans , counta + counto)
            j += 1
        return ans
