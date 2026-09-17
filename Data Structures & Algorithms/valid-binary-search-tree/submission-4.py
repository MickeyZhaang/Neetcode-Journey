# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, val):
            if not root or not (root.left or root.right):
                return True
            if root.val == val:
                return False
            if root.left and root.right:
                if root.left.val < root.val < root.right.val:
                    return True
                return False
            elif root.left:
                if root.left.val < root.val:
                    return True
                return False
            else:
                if root.val < root.right.val:
                    return True
                return False
            return self.isValidBST(root.left, min(root.val, val)) and self.isValidBST(root.right, max(root.val, val))
        return dfs(root, 0)