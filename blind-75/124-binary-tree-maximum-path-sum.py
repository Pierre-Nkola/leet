from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(dfs(root.left),0)
            rightMax = max(dfs(root.right), 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        
        return res[0]

            
sol = Solution()

print(sol.maxPathSum(root = [1,2,3]))


# Helper function to build a binary tree from a list
# def buildTree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
#     if not nodes:
#         return None
#     root = TreeNode(nodes[0])
#     queue = [root]
#     i = 1
#     while i < len(nodes):
#         current = queue.pop(0)
#         if nodes[i] is not None:
#             current.left = TreeNode(nodes[i])
#             queue.append(current.left)
#         i += 1
#         if i < len(nodes) and nodes[i] is not None:
#             current.right = TreeNode(nodes[i])
#             queue.append(current.right)
#         i += 1
#     return root