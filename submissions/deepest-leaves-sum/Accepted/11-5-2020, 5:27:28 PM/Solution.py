// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # preorder(dfs)
        stack = [(root, 0)]
        maxdepth, res = 0, 0
        while stack:
            root, depth = stack.pop()
            if not root:
                continue
            if maxdepth < depth:
                maxdepth = depth
                res = root.val
            elif maxdepth == depth:
                res += root.val
            stack.append((root.left, depth + 1))
            stack.append((root.right, depth + 1))
        return res   