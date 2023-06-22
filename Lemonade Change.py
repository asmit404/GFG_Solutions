'''
Title     : Lemonade Change
Author    : Asmit Singh
Solved On   : 22 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def lemonadeChange(self, N, bills):
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five -= 1
                ten += 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True

# This is the most optimal solution. Just believe me.