// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return False
        elif not t1 or not t2:
            return True
        else:
            return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t2.left, t1.right)
        
        