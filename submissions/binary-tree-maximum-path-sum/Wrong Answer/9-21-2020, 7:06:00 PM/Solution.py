// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def preorder(root: TreeNode) -> int:
            nonlocal res
            if not root:
                return 0
            res = max(res, root.val + preorder(root.left) + preorder(root.right))
            return res
        res = 0
        return preorder(root)