// https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, k: int) -> int:
        cnt = 0
        h = collections.defaultdict(int)
        
        def dfs(root, cursum, h):
            nonlocal cnt
            if not root:
                return
            cursum += root.val
            if cursum == k:
                cnt += 1
            cnt += h[cursum - k]
            h[cursum] += 1 # add this node into consideration
            dfs(root.left, cursum, h)
            dfs(root.right, cursum, h)
            h[cursum] -= 1 # remove this node
            
        dfs(root, 0, h)
        return cnt