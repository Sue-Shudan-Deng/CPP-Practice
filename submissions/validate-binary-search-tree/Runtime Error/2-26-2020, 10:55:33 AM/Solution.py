// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, lower=float("-inf"), upper=float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
    
class Solution(object):
    def isValidBST(self, root):
        stack, inorder = [root], float("-inf")
        while stack or root:
            while root:
                root = root.left
                stack.append(root)
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder, root = root.val, root.right
        return True