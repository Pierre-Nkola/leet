
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, curPath):
            
            if not node: return 
            
            curPath.append(str(node.val))
            
            if not node.left and not node.right:
                res.append("->".join(curPath.copy()))
                
            if node.left: dfs(node.left, curPath)
            if node.right: dfs(node.right, curPath)
            
            curPath.pop()
            
        dfs(root, [])
        return res