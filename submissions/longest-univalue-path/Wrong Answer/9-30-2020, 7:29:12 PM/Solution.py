// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def isUniValue(root: TreeNode) -> bool:
            if not root:
                return False
            if not root.left and not root.right:
                return True
            l = isUniValue(root.left)
            r = isUniValue(root.right)
            if not root.left:
                return r and root.right.val == root.val
            elif not root.right:
                return l and root.left.val == root.val
            else:
                return l and r and root.right.val == root.val and root.val == root.left.val
            
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            flag = True
            if root.left:
                flag = flag and isUniValue(root.left) and root.val == root.left.val
            if root.right:
                flag = flag and isUniValue(root.right) and root.right.val == root.val
            if flag:
                self.ans = max(self.ans, l + r + 1)
            return 1 + max(l, r)
        
        dfs(root)
        return self.ans            