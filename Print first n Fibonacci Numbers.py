"""
Title     : Print first n Fibonacci Numbers
Author    : Asmit Singh
Solved On   : 17 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def printFibb(self, n):
        first, second = 0, 1
        fibonacci_list = []
        for i in range(n):
            fibonacci_list.append(second)
            first, second = second, first + second
        return fibonacci_list

# Time Complexity: O(N)
# Space Complexity: O(N)