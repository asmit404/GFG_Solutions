'''
Title     : Find triplets with zero sum
Author    : Asmit Singh
Solved On   : 8 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def findTriplets(self, arr, n):
        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            seen = set()
            for j in range(i + 1, n):
                complement = -(arr[i] + arr[j])
                if complement in seen:
                    return 1
                seen.add(arr[j])
        return 0
