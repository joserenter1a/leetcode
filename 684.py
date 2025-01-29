# 684. Redundant Connection
# Cycle detection problem
# Union find 



from typing import List 

def findRedundantConnection( edges: List[List[int]]) -> List[int]:
    # maintain the parent of every single node
    N = len(edges)
    par = [i for i in range(N + 1)] # ith node -> parent -> (1 - n)
    # maintain the rank or size of each component
    rank = [1] * (N + 1)

    def find(n):
        if n != par[n]:
            par[n] = find(par[n])
        return par[n]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]