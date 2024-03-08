'''
Title     : Check if frequencies can be equal
Author    : Asmit Singh
Solved On   : 08 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def sameFreq(self, s):
        pool = 'abcdefghijklmnopqrstuvwxyz'
        cnt = [s.count(letter)for letter in pool if s.count(letter) != 0]
        return len(set(cnt)) == 1 or (len(set(cnt)) == 2 and (min(cnt) == 1 or cnt.count(max(cnt)) == 1 and max(cnt) - min(cnt) <= 1))

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)