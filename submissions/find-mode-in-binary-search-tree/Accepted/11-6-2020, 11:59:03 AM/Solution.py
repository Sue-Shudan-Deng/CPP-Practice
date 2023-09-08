// https://leetcode.com/problems/find-mode-in-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        h = collections.defaultdict(int)
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            h[root.val] += 1
            root = root.right
        maxfreq = max([v for k, v in h.items()])
        return [k for k, v in h.items() if v == maxfreq]
        