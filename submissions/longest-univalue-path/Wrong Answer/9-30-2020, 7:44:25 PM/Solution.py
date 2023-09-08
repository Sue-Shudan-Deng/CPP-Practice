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
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            l = dfs(root.left)
            r = dfs(root.right)
            if not root.left:
                if root.right.val == root.val:
                    self.ans = max(self.ans, r + 1)
                    print(self.ans, root.val, r)
                    return r + 1
            elif not root.right:
                if root.left.val == root.val:
                    self.ans = max(self.ans, l + 1)
                    return l + 1
            else:
                if root.left.val == root.val and root.right.val != root.val:
                    self.ans = max(self.ans, l + 1)
                    return 1 + l
                elif root.right.val == root.val and root.left.val != root.val:
                    self.ans = max(self.ans, r + 1)
                    return 1 + r
                elif root.right.val == root.val and root.left.val == root.val:
                    self.ans = max(self.ans, l + r + 1)
                    return max(l, r) + 1
            return 1
        
        dfs(root)
        return self.ans - 1