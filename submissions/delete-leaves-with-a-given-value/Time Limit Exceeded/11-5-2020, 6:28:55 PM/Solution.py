// https://leetcode.com/problems/delete-leaves-with-a-given-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        flag = 1
        def dfs(root: TreeNode, target: int):
            nonlocal flag
            if not root:
                return root
            if not root.left and not root.right and root.val == target:
                flag = 1
                return None
            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)
            return root
        while flag:
            flag = 0
            res = dfs(root, target)
        return res