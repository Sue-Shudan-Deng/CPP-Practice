// https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/house-robber-iii/discuss/376297/Python3-Dynamic-Programming-%2B-Depth-First-Search
        [i, j]: i表示这个节点要用，j表示这个节点不用
        """
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [0, 0]
            l = dfs(root.left)
            r = dfs(root.right)
            #             用root.val                   不用root.val
            return [root.val + l[1] + r[1], max(l[0], l[1]) + max(r[0], r[1])]
        return max(dfs(root))