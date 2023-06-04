'''
Title     : Reversing the equation
Author    : Asmit Singh
Solved On   : 04 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def reverseEqn(self, s):
        arr = []
        seen = set(["+", "-", "*", "/"])
        s = s[::-1]
        i = 0
        while i < len(s):
            if s[i] in seen:
                arr.append(s[i])
            else:
                inter, ia = i, i
                while ia < len(s) and s[ia] not in seen:
                    ia += 1
                    i += 1
                arr.append(s[inter:ia][::-1])
                i -= 1
            i += 1
        return "".join(arr)
