# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxim):
            if not root:
                return 0
            
            is_good = 1 if root.val >= maxim else 0

            new_maxim = max(maxim, root.val)

            return is_good + dfs(root.left, new_maxim) + dfs(root.right, new_maxim)

        return dfs(root, root.val)