// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        def dfs(root, depth, ans):
            if not root:
                return
            if len(ans) < depth + 1:
                ans.append([])
            ans[depth].append(root.val)
            dfs(root.left, depth + 1, ans)
            dfs(root.right, depth + 1, ans)
        dfs(root, 0, ans)
        return ans

# Iterative:
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         ret, level = [], 0
#         queue = collections.deque([root])
#         while queue:
#             ret.append([])
#             level_length = len(queue)
#             for i in range(level_length):
#                 root = queue.popleft()
#                 ret[level].append(root.val)
#                 if root.left: queue.append(root.left)
#                 if root.right: queue.append(root.right)
#             level += 1
#         return ret