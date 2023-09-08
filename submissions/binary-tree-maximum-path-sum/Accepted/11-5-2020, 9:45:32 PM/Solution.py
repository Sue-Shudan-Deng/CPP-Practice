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
        res = float("-inf")
        def maxGain(root):
            nonlocal res
            if not root:
                return 0
            l = max(0, maxGain(root.left))  # 表示left可加可不加
            r = max(0, maxGain(root.right))
            res = max(res, root.val + l + r)
            return root.val + max(l, r) # 满足题目要求，返回的仅有1条路径而不是整棵子树
        maxGain(root)
        return res