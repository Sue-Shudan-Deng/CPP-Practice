// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: 
            return False
        
        if not root.left and not root.right:
            return root.val == sum
        
        l = self.hasPathSum(root.left, sum - root.val)
        r = self.hasPathSum(root.right, sum - root.val)
        
        return l or r