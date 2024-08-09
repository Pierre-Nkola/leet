from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countPaths(node: TreeNode, current_sum: int) -> int:
            if not node: return 0
            
            # Count paths with sum starting from the current node
            current_sum += node.val
            path_count = 0
            if current_sum == targetSum:
                path_count += 1
            
            # Count paths with sum from the left and right subtrees
            if node.left:  path_count += countPaths(node.left, current_sum)
            if node.right: path_count += countPaths(node.right, current_sum)
            
            return path_count
        
        def dfs(node: TreeNode) -> int:
            if not node:return 0
            
            # Count paths that start from the current node
            paths_from_node = countPaths(node, 0)
            
            # Count paths in the left and right subtrees
            paths_from_left = dfs(node.left)
            paths_from_right = dfs(node.right)
            
            return paths_from_node + paths_from_left + paths_from_right
        
        return dfs(root)

 # dictionary optimization
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:      
    #     count = 0
    #     h = defaultdict(int)

    #     def dfs(root, value):
    #         nonlocal count
    #         if not root:
    #             return 
            
    #         value += root.val
    #         if value == targetSum:
    #             count += 1
    #         count += h[value-targetSum]
    #         h[value] += 1

    #         dfs(root.left, value)
    #         dfs(root.right, value)

    #         h[value] -= 1
 
    #     dfs(root, 0)
    #     return count