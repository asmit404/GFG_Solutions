'''
Title     : Expression Add Operators
Author    : Asmit Singh
Solved On   : 25 May 2023
Solved Using   : Python3
'''

class Solution:
    def addOperators(self, s, target):
        n = len(s)
        ans = []
        
        def res(i, path, result, prev):
            if i == n:
                if result == target:
                    ans.append(path)
                return

            for j in range(i+1, n+1):
                if j > i+1 and s[i] == '0':
                    break
                num = int(s[i:j])
                if i == 0:
                    res(j, path + str(num), result + num, num)
                else:
                    res(j, path + "+" + str(num), result + num, num)
                    res(j, path + "-" + str(num), result - num, -num)
                    res(j, path + "*" + str(num), result - prev + prev*num, prev*num)

        res(0, "", 0, 0)
        return ans
