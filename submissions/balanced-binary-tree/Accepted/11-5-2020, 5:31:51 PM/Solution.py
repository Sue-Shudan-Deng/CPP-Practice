// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            return max(l, r) + 1
        
        return abs(height(root.left) - height(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)