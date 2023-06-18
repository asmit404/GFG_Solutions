'''
Title     : Ticket Counter
Author    : Asmit Singh
Solved On   : 18 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def distributeTicket(self, N: int, K: int) -> int:
        arr = [i for i in range(1, N+1)]
        def ticket(arr, k):
            if len(arr) <= k:
                return arr[-1]
            var = ticket(arr[k:][::-1], k)
            return var
        return ticket(arr, K)

# Not the most kawaii program structure, but it works... I think.