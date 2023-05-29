'''
Title     : CamelCase Pattern Matching
Author    : Asmit Singh
Solved On   : 29 May 2023
Solved Using   : Python3
'''

class Solution:
    def CamelCase(self, N, Dictionary, Pattern):
        ans = []
        for word in Dictionary:
            str = ""
            for char in word:
                if ord(char) > 64 and ord(char) < 91:
                    str += char
                    if str == Pattern:
                        ans.append(word)
                        break
        if len(ans) == 0:
            return [-1]
        return ans
