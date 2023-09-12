"""
Title     : Perfect Numbers
Author    : Asmit Singh
Solved On   : 12 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def isPerfectNumber(self, num):
        if num <= 1:
            return 0
        divisor = 1
        sum_of_divisors = 0
        while divisor**2 <= num:
            if num % divisor == 0:
                sum_of_divisors += divisor
                if divisor != 1 and divisor**2 != num:
                    sum_of_divisors += num // divisor
            divisor += 1
        return 1 if sum_of_divisors == num else 0

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)