// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxGain(root):
            global res
            if not root:
                return 0
            left = maxGain(root.left)
            right = maxGain(root.right)
            
            res = max(res, left + right)
            
            return max(left, right) + 1
        
        global res
        res = 0
        maxGain(root)
        return res