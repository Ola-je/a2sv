# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(node, min_ = float('-inf'), max_ = float('inf')):
            if not node:
                return True

            if not(min_ < node.val < max_):
                return False
           
            return (checker(node.left, min_, node.val) and checker(node.right, node.val,max_))
        return checker(root)
                