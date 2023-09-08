// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float("-inf")
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        def count(root):
            nonlocal res
            if not root:
                return 0
            l = count(root.left)
            r = count(root.right)
            res = max(res, 1 + l + r)
            return 1 + max(l, r)
        count(root)
        return res - 1