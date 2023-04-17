'''
Title     : Job Sequencing Problem
Domain    : Dynamic Programming, Greedy, Algorithms
Author    : Asmit Singh
Solved On   : 17 Apr 2023
Solved Using   : Python3
'''

class Solution:
    def JobScheduling(self, Jobs, n):
        jobs = []
        maxtime = 0
        for i in range(n):
            maxtime = max(maxtime, Jobs[i].deadline)
            jobs.append([Jobs[i].id, Jobs[i].deadline, Jobs[i].profit])
        jobs.sort(key=lambda x: x[2], reverse=True)
        no_jobs = 0
        visited = [False]*(maxtime+1)
        max_profit = 0
        for i in jobs:
            for j in range(i[1], 0, -1):
                if (visited[j] == False):
                    visited[j] = True
                    no_jobs += 1
                    max_profit += i[2]
                    break
        return [no_jobs, max_profit]
