// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        res = []
        def dfs(root, depth):
            # from right subtree
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        dfs(root, 0)
        return res