// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root or root == p or root == q:
                return root
            left = search(root.left, p, q)
            right = search(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        return search(root, p, q)