// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            root_idx = mapping[root_val]
            root.left = helper(left_idx, root_idx-1)
            root.right = helper(root_idx+1, right_idx)
            return root
            
        mapping = {v:k for k,v in enumerate(inorder)}
        preorder = deque(preorder)
        return helper(0, len(preorder)-1)