// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # [i, j1, j2]: i表示这个点要用，j1表示这个点不用并且这个点被下面的点cover到了，j2表示这个点不用并且没有被下面的点cover到
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        def dfs(root):
            if not root:
                return [float("inf"), 0, 0]
            l = dfs(root.left)
            r = dfs(root.right)
            return [1 + min(l) + min(r),
                    min(l[0] + min(r[1:]), r[0] + min(l[1:])),
                    l[1] + r[1]]
        
        return min(dfs(root)[:-1])