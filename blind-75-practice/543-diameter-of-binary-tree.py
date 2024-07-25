from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # Compute the depth of the left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter at this node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the depth of the node
            # This is where the depth is incremented as we go down the tree
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter

# Example usage:
# Constructing the binary tree: [1,2,3,4,5]
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3
