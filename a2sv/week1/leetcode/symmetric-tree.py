# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        def leftRight(node):
            if not node:
                stack1.append(None)
                return
            stack1.append(node.val)
            leftRight(node.left)
            leftRight(node.right)
        def rightLeft(node):
            if not node:
                stack2.append(None)
                return
            stack2.append(node.val)
            rightLeft(node.right)
            rightLeft(node.left)
        leftRight(root)
        rightLeft(root)

        i = 0
        while stack1 and stack2 and i < len(stack1):
            if stack1[i] != stack2[i]:
                return False
            i +=1
        return True
            
