"""
Title     : Smith Number
Author    : Asmit Singh
Solved On   : 09 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def smithNum(self, n):
        def sum_of_digits(x): 
            return sum(int(i) for i in str(x))
        res = sum_of_digits(n)
        var = 0
        for i in range(2, n):
            if n <= 1:
                break
            while n > 1 and n % i == 0:
                n //= i
                var += sum_of_digits(i)
        return int(var == res)

# Time Complexity  : O(n)
# Space Complexity : O(1)