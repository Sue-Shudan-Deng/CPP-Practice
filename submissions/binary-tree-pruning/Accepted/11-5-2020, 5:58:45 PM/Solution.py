// https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def containsOne(root):
            if not root:
                return False
            l = containsOne(root.left)
            r = containsOne(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None
            return root.val or l or r
        return root if containsOne(root) else None