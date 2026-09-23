# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not root or not (root.left or root.right):
                return True
            lower = root.left.val if root.left else lower
            upper = root.right.val if root.right else upper
            if not (lower < root.val < upper):
                return False
            return (
                dfs(root.left, max(lower, root.val), root.val) and
                dfs(root.right, root.val, min(upper, root.val))
            )
        return dfs(root, float("-inf"), float("inf"))