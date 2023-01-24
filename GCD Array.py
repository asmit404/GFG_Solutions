'''
Title     : GCD Array
Domain    : Arrays, Mathematical, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 22 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        a=sum(arr)
        m=int(a**0.5)
        d=[]
        for i in range(1,m+1):
            if a%i==0:
                d.append(i)
                if i!=a//i:
                    d.append(a//i)
        d.sort(reverse=True)
        for i in range(1,N):
            arr[i]+=arr[i-1]
        res=1
        for x in d:
            cnt=0
            for y in arr:
                if (y%x)==0:
                    cnt+=1
            if cnt>=K:
                res=x
                break
        return res
