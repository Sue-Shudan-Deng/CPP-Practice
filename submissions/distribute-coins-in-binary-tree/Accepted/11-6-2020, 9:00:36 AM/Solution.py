// https://leetcode.com/problems/distribute-coins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        """
        https://www.youtube.com/watch?v=zQqku1AXVF8
        """
        flow = 0
        def extraCoinNum(root):
            nonlocal flow
            if not root:
                return 0
            l = extraCoinNum(root.left)
            r = extraCoinNum(root.right)
            flow += (abs(l) + abs(r))
            return l + r + root.val - 1
        extraCoinNum(root)
        return flow