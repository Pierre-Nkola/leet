from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node: TreeNode, curList: list):
            
            if not node: return 
            
            curList.append(str(node.val))
            
            if not node.left and not node.right:
                res.append("".join(curList.copy()))
                
            if node.left: dfs(node.left, curList)
            if node.right: dfs(node.right, curList)
            
            curList.pop()
            
        dfs(root, [])
        total = 0
        for num in res:
            total += int(num)
        return total
    
        # ["123", "456", "90"]