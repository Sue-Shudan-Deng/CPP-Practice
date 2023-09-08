// https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans, prev = float("inf"), float("inf") 
        if not root:
            return 0
        def dfs(root):
            nonlocal ans, prev
            # inorder
            if not root:
                return
            dfs(root.left)
            ans = min(ans, abs(prev - root.val))
            prev = root.val
            dfs(root.right)
        dfs(root)
        return ans
            
            