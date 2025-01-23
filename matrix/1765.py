from typing import List 
from collections import deque

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    rows, cols = len(isWater), len(isWater[0])
    q = deque()
    height = [[-1] * cols for _ in range(rows)] #-1 = unvisited sposts

    #enqueue all water cells
    for r in range(rows):
        for c in range(cols):
            if isWater[r][c]:
                q.append((r, c))
                height[r][c] = 0
    
    # BFS
    while q:
        r, c = q.popleft()
        h = height[r][c]

        neighbors = [[r + 1, c], [r, c + 1], [r-1, c], [r, c-1]]
        for nr, nc in neighbors:
            if (nr < 0 or nc < 0 or 
                nr == rows or nc == cols or
                height[nr][nc] != -1 
                ):
                continue
            q.append((nr, nc))
            height[nr][nc] = h + 1
    return height