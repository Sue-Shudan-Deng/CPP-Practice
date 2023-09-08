// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0
        def countUnival(root):
            nonlocal ans
            if not root:
                return 0
            if not root.left and not root.right:
                ans = max(ans, 1)
                return 1
            l = countUnival(root.left)
            r = countUnival(root.right)
            if not root.left:
                if root.right.val == root.val:
                    ans = max(ans, r + 1)
                    return r + 1
            elif not root.right:
                if root.left.val == root.val:
                    ans = max(ans, l + 1)
                    return l + 1
            else:
                if root.left.val == root.val and root.right.val != root.val:
                    ans = max(ans, l + 1)
                    return 1 + l
                elif root.right.val == root.val and root.left.val != root.val:
                    ans = max(ans, r + 1)
                    return 1 + r
                elif root.right.val == root.val and root.left.val == root.val:
                    ans = max(ans, l + r + 1)
                    return max(l, r) + 1
            return 1
        
        countUnival(root)
        return ans - 1 if root else 0