"""
LeetCode #449. Serialize and Deserialize BST
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
     def __str__(self):
        return f'TreeNode({self.val})'
     def __repr__(self):
        return f'TreeNode({self.val})'

from typing import List

def serialize(root: List[TreeNode]) -> str:
    """Encodes a tree to a single string.
    """
    res = []
    def dfs(node):
        if not node:
            res.append("N")
            return 
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(res)



def deserialize(data: str) -> List[TreeNode]:
    """Decodes your encoded data to tree.
    """
    vals = data.split(',')
    self.i = 0
    def dfs():
        if vals[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(vals[self.i]))
        self.i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()


root = [TreeNode(1), TreeNode(2), TreeNode(3)]
sol  = serialize(root)
print(sol)

sol2 = deserialize(sol)
print(sol2)