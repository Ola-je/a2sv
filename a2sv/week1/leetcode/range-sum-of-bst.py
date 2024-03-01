# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def added(node):
            nonlocal result
            if not node:
                return
            if node.val >= low and node.val <= high:
                result += node.val
                added(node.left)
                added(node.right)
            elif node.val < low:
                added(node.right)
            elif node.val > high:
                added(node.left)
        result = 0
        added(root)
        return result
