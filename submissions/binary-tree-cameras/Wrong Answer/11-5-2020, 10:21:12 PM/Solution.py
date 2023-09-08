// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # [i, j]: i表示这个点用，j表示这个点不用
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        def dfs(root):
            if not root:
                return [0, 0]
            l = dfs(root.left)
            r = dfs(root.right)
            #                用root.val                    不用root.val
            return [1 + min(l[0], l[1]) + min(r[0], r[1]), l[0] + r[0]]
        
        return min(dfs(root))