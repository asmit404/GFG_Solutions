'''
Title     : Last cell in a Matrix
Domain    : Matrix, Data Structures
Author    : Asmit Singh
Solved On   : 03 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def endPoints(self, matrix, R, C):
        y, x, m = 0, 0, 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]        
        while True:
            while 0 <= y < R and 0 <= x < C and matrix[y][x] == 0:
                y += move[m][0]
                x += move[m][1]
            else:
                if y < 0 or y == R or x < 0 or x == C:
                    return (y-move[m][0], x-move[m][1])
                else:
                    matrix[y][x] = 0
                    m = (m + 1) % 4
