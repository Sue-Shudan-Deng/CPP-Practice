// https://leetcode.com/problems/inorder-successor-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        hot = None
        while root:
            if root.val > p.val:
                hot = root
                root = root.left
            else:
                root = root.right
        return hot