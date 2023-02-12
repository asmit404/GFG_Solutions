'''
Title     : Case-Specific Sorting of Strings
Domain    : Strings, Sorting, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 26 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def caseSort(self,s,n):
        dic1 = {}
        dic2 = {}
        ans = []
        for ele in s:
            if ord(ele) < 97:
                if ele in dic1:
                    dic1[ele] += 1
                    continue
                dic1[ele] = 1
            else:
                if ele in dic2:
                    dic2[ele] += 1
                    continue
                dic2[ele] = 1
        
        dic3 = list(dic1.keys())
        dic4 = list(dic2.keys())
        dic3.sort()
        dic4.sort()
    
        i = 0
        j = 0
        for ele in s:
            if ord(ele) < 97:
                gle = dic3[i]
                if dic1[gle] > 1:
                    ans.append(dic3[i])
                    dic1[gle] -= 1
                    continue
                ans.append(dic3[i])
                i += 1
                    
            else:
                gle = dic4[j]
                if dic2[gle] > 1:
                    ans.append(dic4[j])
                    dic2[gle] -= 1
                    continue
                ans.append(dic4[j])
                j += 1
        
        return "".join(ans)
