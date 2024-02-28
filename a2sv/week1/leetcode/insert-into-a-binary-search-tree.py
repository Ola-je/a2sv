# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(node, key):
            if not node:
                node = TreeNode(key)
                return node
            if node.val > key:
                node.left = insert(node.left,key)
                return node
            elif node.val < key:
                node.right = insert(node.right, key)
                return node
        return insert(root, val)
        
