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
            left = dfs(root.left)
            right = dfs(root.right)
            #             用root.val                       不用root.val
            x = [root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])]
            return x
        
        return max(dfs(root))