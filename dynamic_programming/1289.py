"""
LeetCode #1289. Min falling Path Sum II

Author: Jose Renteria
"""
from typing import List
def minFallingPathSum(self, grid: List[List[int]]) -> int:
    N = len(grid)
    cache = {}
    def helper(r, c):
        if r == N - 1:
            return grid[r][c]
        if (r, c) in cache:
            return cache[(r, c)]
        res = float('inf')
        for next_col in range(N):
            if c != next_col:
                res = min(
                    res, grid[r][c]+ helper(r + 1, next_col)
                )
        cache[(r, c)] = res
        return res
    res = float('inf')
    for col in range(N):
        res = min(res, helper(0, col))
    return res