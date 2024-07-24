from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0, True
            
            left_height, left_balanced = dfs(root.left)
            right_height, right_balanced = dfs(root.right)
            
            height = max(left_height, right_height) + 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return height, balanced
        
        _, result = dfs(root)
        return result
