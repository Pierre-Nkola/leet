# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, newtarget):
            
            if not node:
                return False
            
            if not node.left and not node.right:
                return newtarget == node.val
            
            return dfs(node.left, newtarget - node.val) or dfs(node.right, newtarget - node.val)
        
        return dfs(root, targetSum)