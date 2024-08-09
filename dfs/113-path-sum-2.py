from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curList, newTarget):
            
            if not node: return 
            
            curList.append(node.val)
            
            if not node.left and not node.right and node.val == newTarget:
                res.append(curList.copy())
            
            
            dfs(node.left, curList, newTarget - node.val)
            dfs(node.right, curList, newTarget - node.val)
            
            curList.pop()
            
        dfs(root, [], targetSum)
        return res
    

sol = Solution()

# Create a binary tree:
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \      \
#7    2      1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(sol.pathSum(root, 22))  # Output: [[5, 4, 11, 2], [5, 8, 4, 1]]