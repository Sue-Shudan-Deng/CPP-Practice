// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxGain(root):
            global res
            if not root:
                return 0
            
            left = max(0, maxGain(root.left))
            right = max(0, maxGain(root.right))
            
            res = max(res, root.val + left + right)
            
            return root.val + max(left, right)
        
        global res
        res = 0
        maxGain(root)
        return res