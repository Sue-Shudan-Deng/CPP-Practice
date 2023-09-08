// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        注：和maximum depth做法完全一样，都是先序遍历
        """
        if not root:
            return False
        stack = [(root, summ)]
        while stack:
            root, summ = stack.pop()
            summ -= root.val
            if not root.left and not root.right and summ == 0:
                return True
            if root.right:
                stack.append((root.right, summ))
            if root.left:
                stack.append((root.left, summ))
        return False