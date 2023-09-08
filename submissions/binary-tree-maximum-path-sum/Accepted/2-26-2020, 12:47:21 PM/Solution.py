// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        这道题不太好想，需要反复练习
        """
        def maxGain(node):
            nonlocal res
            if not node:
                return 0
            # 0 here means if some path < 0, there is no need to add it on
            left = max(0, maxGain(node.left))
            right = max(0, maxGain(node.right))
            ################
            res = max(res, node.val + left + right)
            ################
            
            return node.val + max(left, right)
        res = root.val
        maxGain(root)
        return res