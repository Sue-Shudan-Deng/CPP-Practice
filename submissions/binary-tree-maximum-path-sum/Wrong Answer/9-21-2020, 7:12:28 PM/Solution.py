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
            left = max(0, preorder(root.left))
            right = max(0, preorder(root.right))
            cur = root.val + left + right
            res = max(res, cur)
            return cur
        res = float("-inf")
        preorder(root)
        return res