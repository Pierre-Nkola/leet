class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self,val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k:int):
        n = 0
        stack = []
        cur = root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.next 
            n += 1
            cur = stack.pop()
            if n == k:
                return cur.val
            cur= cur.right