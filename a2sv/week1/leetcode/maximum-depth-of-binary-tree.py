# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        
        def calc(node, count):
            if not node:
                self.max_val= max(self.max_val, count)
                return

            calc(node.left, count +1)
            calc(node.right, count+1)
        calc(root, 0)
        return self.max_val