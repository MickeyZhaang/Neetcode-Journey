# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxim = 0

        def dfs(root):
            if not root:
                return -1
            
            h1 = dfs(root.left) + 1
            h2 = dfs(root.right) + 1

            path = h1 + h2
            self.maxim = max(self.maxim, path)

            return max(h1, h2)

        dfs(root)

        return self.maxim
