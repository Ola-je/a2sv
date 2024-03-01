# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(node):
            if not node:
                return
            arr.append(node.val)
            inorder(node.left)
            inorder(node.right)
        inorder(root)

        dic = Counter(arr)
        max_ = max(dic.values())
        result = []

        for i in dic:
            if dic[i] == max_:
                result.append(i)
        return result

        