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
        def helper(root, lower=float("-inf"), upper=float("inf")):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
        return helper(root)
    
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Iteration + inorder
        """
        if not root:
            return True
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True