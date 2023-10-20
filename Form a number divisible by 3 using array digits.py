"""
Title     : Form a number divisible by 3 using array digits
Author    : Asmit Singh
Solved On   : 20 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def isPossible(self, N, arr):
        return 1 if sum(int(digit) for num in arr for digit in str(num)) % 3 == 0 else 0

# Time Complexity: O(N)
# Space Complexity: O(1)