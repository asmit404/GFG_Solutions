'''
Title     : Distinct Difference
Domain    : Set, Arrays, Map, Data Structures
Author    : Asmit Singh
Solved On   : 18 Mar 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def getDistinctDifference(self, N: int, A: List[int]) -> List[int]:
        newArr = []
        setArr = set()
        dic = {}
        x = len(list(set(A[1:])))
        newArr.append(0-x)
        setArr.add(A[0])
        for i in range(1, N):
            if A[i] not in dic:
                dic[A[i]] = 1
            else:
                dic[A[i]] += 1
        cnt = len(dic)
        for i in range(1, N-1):
            if dic[A[i]] == 1:
                cnt -= 1
            else:
                dic[A[i]] -= 1
            newArr.append(len(setArr) - cnt)
            setArr.add(A[i])
        newArr.append(len(setArr))
        return newArr
