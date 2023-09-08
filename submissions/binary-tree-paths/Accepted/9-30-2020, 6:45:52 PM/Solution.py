// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = [] 
        def dfs(root, cur, ans):
            if not root:
                return
            if not root.left and not root.right:
                ans.append("".join([str(i) + "->" for i in cur[:]] + [str(root.val)]))
                return
            cur.append(root.val)
            dfs(root.left, cur, ans)
            dfs(root.right, cur, ans)
            cur.pop()
            
        dfs(root, [], ans)
        return ans