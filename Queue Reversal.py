'''
Title     : Queue Reversal
Author    : Asmit Singh
Solved On   : 16 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def rev(self, q):
        stack = []
        while not q.empty():
            stack.append(q.get())
        while stack:
            q.put(stack.pop())
        return q

# IDFK why, but this took 5.74 seconds to execute.
# If you have something better, send a PR.