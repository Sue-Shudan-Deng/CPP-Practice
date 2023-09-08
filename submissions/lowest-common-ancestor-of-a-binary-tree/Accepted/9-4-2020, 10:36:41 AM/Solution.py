// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果在该树中找p, q
        # 一个都没找到：返回none
        # 只找到一个：返回找到的这个值所在的节点
        # 找到两个，返回lca; 特别的，如果恰好一个在左边一个在右边(即split),则返回root node
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right