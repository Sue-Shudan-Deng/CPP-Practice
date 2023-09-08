// https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # 无论是哪种搜索路径，一定包含根结点
        closest = float("inf")
        while root:
            closest = min(closest, root.val, key = lambda x: abs(x-target))
            root = root.left if target < root.val else root.right
        return closest