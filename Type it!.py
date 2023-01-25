'''
Title     : Type it!
Domain    : Strings, Data Structures
Author    : Asmit Singh
Solved On   : 25 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def minOperation(self, s): 
        var1 = ""
        var2 = ""
        for i in range(len(s)):
            var2+=s[i]
            if var2 in s[i+1:]:
                var1 = var2
        if len(var1)!=0:
            return (len(s)-len(var1)+1)
        else:
            return len(s)
        return len(s)
