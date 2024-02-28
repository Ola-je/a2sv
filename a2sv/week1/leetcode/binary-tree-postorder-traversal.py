# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def traversed(node):
            if not node:
                return
            traversed(node.left)
            traversed(node.right)
            arr.append(node.val)
        traversed(root)
        return arr