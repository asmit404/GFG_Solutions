'''
Title     : Print matrix in diagonal pattern
Author    : Asmit Singh
Solved On   : 13 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def matrixDiagonally(self, mat):
        n = len(mat)
        i = j = k = 0
        isUp = True
        res = []

        while k < n * n:
            if isUp:
                while i >= 0 and j <= n - 1:
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
                    k += 1

                if i < 0 and j <= n - 1:
                    i = 0

                if j == n:
                    i += 2
                    j -= 1

            else:
                while j >= 0 and i <= n - 1:
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
                    k += 1

                if j < 0 and i <= n - 1:
                    j = 0

                if i == n:
                    j += 2
                    i -= 1

            isUp = not isUp
        return res

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)