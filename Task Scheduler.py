'''
Title     : Task Scheduler
Author    : Asmit Singh
Solved On   : 23 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def leastInterval(self, N, K, tasks):
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        maxi = max(freq)
        nof = freq.count(maxi)
        res = (maxi - 1) * (K + 1) + nof
        return max(N, res)
