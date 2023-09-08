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
            
            return [root.val + left[1] + right[1], left[0] + right[0]]
        
        return max(dfs(root))