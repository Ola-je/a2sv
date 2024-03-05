# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = TreeNode()
        def helper(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                return helper(node.right)
            else:
                return helper(node.left)
        return helper(root)
