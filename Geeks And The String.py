'''
Title     : Geeks And The String
Domain    : Stack, Data Structures
Author    : Asmit Singh
Solved On   : 23 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def removePair(self,s):
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        if len(stack)>0:
            return "".join(stack)
        else:
            return "-1"
