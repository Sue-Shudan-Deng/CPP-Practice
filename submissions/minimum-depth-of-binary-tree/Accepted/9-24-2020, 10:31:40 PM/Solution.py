// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        leftmin = self.minDepth(root.left)
        rightmin = self.minDepth(root.right)
        if not root.right:
            return leftmin + 1
        elif not root.left:
            return rightmin + 1
        else:
            return min(leftmin, rightmin) + 1