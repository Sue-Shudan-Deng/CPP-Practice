// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        1. 分别判断左右子树是否valid
        2. 分别求出左右子树的最大和最小值，和根结点比较
        """
        # Edge case
        if not root or (not root.left and not root.right):
            return True
        
        def minBST(root):
            while root.left:
                root = root.left
            return root
        
        def maxBST(root):
            while root.right:
                root = root.right
            return root
        
        left_max_valid = maxBST(root.left).val < root.val if root.left else True
        right_min_valid = root.val < minBST(root.right).val if root.right else True
        
        return self.isValidBST(root.left) and self.isValidBST(root.right) and left_max_valid and right_min_valid
        