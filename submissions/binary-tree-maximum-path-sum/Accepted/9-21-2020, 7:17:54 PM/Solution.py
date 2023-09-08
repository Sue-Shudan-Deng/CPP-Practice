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
        这道题还真不太好想，需要反复练习
        """
        self.res = float("-inf")
        def maxGain(node):
            if not node:
                return 0
            left = max(0, maxGain(node.left))  # 技巧2，表示left可加可不加
            right = max(0, maxGain(node.right))
            ################
            self.res = max(self.res, node.val + left + right)
            ################
            return node.val + max(left, right) # 技巧3，满足题目要求，返回的仅有1条路径而不是整棵子树
        maxGain(root)
        return self.res