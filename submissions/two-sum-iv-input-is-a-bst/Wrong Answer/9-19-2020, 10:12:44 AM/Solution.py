// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root: TreeNode) -> List[int]:
            if not root: return []
            s, ans = [], []
            while root or s:
                while root:
                    s.append(root)
                    root = root.left
                root = s.pop()
                ans.append(root.val)
                root = root.right
            return ans
        def sortedTwoSum(x: List[int], target: int) -> bool:
            if not x: return False
            l, r = 0, len(x) - 1
            while l <= r:
                if x[l] + x[r] > target:
                    r -= 1
                elif x[l] + x[r] < target:
                    l += 1
                else:
                    return True
            return False
        
        return sortedTwoSum(inorder(root), k)     
                