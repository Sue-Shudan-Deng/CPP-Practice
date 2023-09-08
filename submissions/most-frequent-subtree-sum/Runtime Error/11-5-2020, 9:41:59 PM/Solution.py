// https://leetcode.com/problems/most-frequent-subtree-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res = collections.defaultdict(int)
        def TreeSum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                res[root.val] += 1
                return root.val
            l = TreeSum(root.left)
            r = TreeSum(root.right)
            summ = l + r + root.val
            res[summ] += 1
            return summ
        TreeSum(root)
        maxfreq = max(res.values())
        return [k for k, v in res.items() if v == maxfreq]
        
            
            
            
            
            
            