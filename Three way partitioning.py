'''
Title     : Three way partitioning
Author    : Asmit Singh
Solved On   : 21 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def threeWayPartition(self, array, a, b, i = 0):
        low, high = 0, len(array) - 1
        while i <= high:
            if array[i] < a:
                array[i], array[low] = array[low], array[i]
                low += 1
                i += 1
            elif array[i] > b:
                array[i], array[high] = array[high], array[i]
                high -= 1
            else:
                i += 1

# Time Complexity: O(n)
# Space Complexity: O(1)