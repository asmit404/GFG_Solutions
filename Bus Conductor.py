'''
Title     : Bus Conductor
Author    : Asmit Singh
Solved On   : 21 May 2023
Solved Using   : Python3
'''

class Solution:
    def findMoves(self, n, chairs, passengers):
        chairs.sort()
        passengers.sort()
        count = 0
        for i in range(n):
            count += abs(passengers[i]-chairs[i])
        return count
