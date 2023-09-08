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
        def count(root):
            if not root:
                return 0
            left = count(root.left)
            right = count(root.right)
            self.res = max(self.res, 1 + left + right)
            return 1 + max(left, right)
        count(root)
        return self.res - 1