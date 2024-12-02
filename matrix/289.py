"""
LeetCode 289: Game of Life

Author: Jose Renteria
"""
from typing import List
def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def count_neighbors(r, c):
        nei = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 or
                    i == M or j == N): continue
                if board[i][j] in [1, 3]: nei += 1
        return nei


    M, N = len(board), len(board[0])
    for row in range(M):
        for col in range(N):
            nb = count_neighbors(row, col)
            if board[row][col] : #equal to a 1
                if nb in [2, 3]:
                    board[row][col] = 3
                
            elif nb == 3:
                    board[row][col] = 2
    for row in range(M):
        for col in range(N):
            if board[row][col] == 1:
                board[row][col] == 0
            
            elif board[row][col] in [2, 3]:
                board[row][col] = 1