"""
Title     : Sum-string
Author    : Asmit Singh
Solved On   : 04 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def isSumString(self, S):
        def check_string(i, j, k, S):
            if k == len(S): return True
            elif k > len(S): return False
            str1 = int(S[i:j])
            str2 = int(S[j:k])
            str3 = str(str1 + str2)

            if not S[k:].startswith(str3): return False
            return check_string(j, k, k + len(str3), S)

        for i in range(1, len(S)):
            for j in range(i+1, len(S)):
                if check_string(0, i, j, S):
                    return 1
        return 0

# Time Complexity  : O(n^3)
# Space Complexity : O(n)