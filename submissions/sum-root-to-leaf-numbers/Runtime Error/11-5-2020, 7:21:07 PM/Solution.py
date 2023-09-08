// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        summ = 0
        def dfs(root: TreeNode, cur: List[int]):
            if not root:
                return
            if not root.left and not root.right:
                cur.append(str(root.val))
                summ += int("".join(cur[:]))
                cur.pop()
                return
            cur.append(str(root.val))
            dfs(root.left, cur)
            dfs(root.right, cur)
            cur.pop()
            
        dfs(root, [])
        return summ