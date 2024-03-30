"""
LeetCode #73. Set Matrix Zeroes

Author: Jose Renteria
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arri, arrj = [], []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    arri.append(i)
                    arrj.append(j)
        for i in range(rows):
            for j in range(cols):
                if(i in arri or j in arrj):
                    matrix[i][j] = 0
