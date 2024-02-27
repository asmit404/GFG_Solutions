"""
Title     : Play With OR
Author    : Asmit Singh
Solved On   : 27 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def game_with_number (self, arr,  n) : 
        for i in range(n - 1):
            arr[i] |= arr[i + 1]
        return arr

# Time Complexity: O(n)
# Space Complexity: O(1)