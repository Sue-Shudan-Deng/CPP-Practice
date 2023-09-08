// https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # method 1: 560 number of subarray sum equal k  
#     def pathSum(self, root: TreeNode, k: int) -> int:
#         cnt = 0
#         h = collections.defaultdict(int)
        
#         def dfs(root, cursum, h):
#             nonlocal cnt
#             if not root:
#                 return
#             cursum += root.val
#             if cursum == k:
#                 cnt += 1
#             cnt += h[cursum - k]
#             h[cursum] += 1 # add this node into consideration
#             dfs(root.left, cursum, h)
#             dfs(root.right, cursum, h)
#             h[cursum] -= 1 # remove this node
            
#         dfs(root, 0, h)
#         return cnt
    
    # method 2: Path sum I with modification, https://www.youtube.com/watch?v=EE8S0pAi_dM
    def pathSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        def dfs(root, rest):
            # start from an arbitrary root, count the number of sum k
            if not root:
                return 0
            rest -= root.val
            tmp = 1 if rest == 0 else 0
            return tmp + dfs(root.left, rest) + dfs(root.right, rest)
            
        return dfs(root, k) + self.pathSum(root.left, k) + self.pathSum(root.right, k)
        