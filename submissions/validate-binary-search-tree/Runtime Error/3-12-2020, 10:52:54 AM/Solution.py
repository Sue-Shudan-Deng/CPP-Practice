// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Recursion
        """
        def helper(root, left = float("-inf"), right = float("inf")):
            if not root:
                return True
            if root.val <= left or root.val >= upper:
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        return helper(root)