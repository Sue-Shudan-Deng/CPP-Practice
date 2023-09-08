// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Recursion
        """
        if not root:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root
    
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         """
#         Iteration
#         """
#         while root and root.val != val:
#             root = root.left if val < root.val else root.right
#         return root