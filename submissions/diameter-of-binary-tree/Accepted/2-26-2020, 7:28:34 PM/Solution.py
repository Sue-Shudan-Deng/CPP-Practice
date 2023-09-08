// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxdepth(node):
            nonlocal res
            if not node:
                return 0
            left = maxdepth(node.left)
            right = maxdepth(node.right)
            
            res = max(res, left + right)
            
            return max(left, right) + 1
        res = 0
        maxdepth(root)
        return res