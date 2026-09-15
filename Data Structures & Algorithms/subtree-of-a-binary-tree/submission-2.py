# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            if not (p and q):
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        if not root:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right or sameTree(root, subRoot)
                