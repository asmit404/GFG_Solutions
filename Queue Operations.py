'''
Title     : Queue Operations
Author    : Asmit Singh
Solved On   : 17 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def insert(self, q, k):
        q.append(k)

    def findFrequency(self, q, k):
        return q.count(k)

# Did they run out of questions or something?