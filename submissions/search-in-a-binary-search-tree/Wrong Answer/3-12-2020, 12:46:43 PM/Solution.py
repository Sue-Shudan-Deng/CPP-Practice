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
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)
    
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Iteration
        """
        while root and root.val != root:
            root = root.left if val < root.val else root.right
        return root