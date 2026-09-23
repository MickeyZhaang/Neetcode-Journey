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
            lower = root.left.val if root.left and lower == float("-inf") else lower
            upper = root.right.val if root.right and upper == float("inf") else upper
            print(f"lower: {lower} and upper: {upper}, root: {root.val}")
            if not (lower < root.val < upper):
                return False
            return (
                dfs(root.left, lower, root.val) and
                dfs(root.right, root.val, upper)
            )
        return dfs(root, float("-inf"), float("inf"))