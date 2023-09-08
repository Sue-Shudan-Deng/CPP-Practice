// https://leetcode.com/problems/range-sum-query-mutable

class SegmentTreeNode:
    def __init__(self, start, end, summ, left=None, right=None):
        self.start = start
        self.end = end
        self.summ = summ
        self.left = left
        self.right = right

def buildSegmentTree(start, end, nums):
    if start == end:
        return SegmentTreeNode(start, start, nums[start])
    mid = start + (end - start) // 2
    l = buildSegmentTree(start, mid, nums)
    r = buildSegmentTree(mid + 1, end, nums)
    return SegmentTreeNode(start, end, l.summ + r.summ, l, r)

def UpdateTree(root, index, val):
    if root.start == index and root.end == index:
        root.summ = val
        return
    mid = root.start + (root.end - root.start) // 2
    if index <= mid:
        UpdateTree(root.left, index, val)
    else:
        UpdateTree(root.right, index, val)
    root.summ = root.left.summ + root.right.summ
    
def QuerySum(root, i, j):
    if root.start == i and root.end == j:
        return root.summ
    m = root.start + (root.start - root.end) // 2
    if j <= m: # i <= m and j <= m
        return QuerySum(root.left, i, j)
    elif i > m: # i > m and j > m
        return QuerySum(root.right, i, j)
    else: # i <= m and j > m
        return QuerySum(root.left, i, m) + QuerySum(root.right, m + 1, j)

class NumArray:
    def __init__(self, nums: List[int]):
        if nums:
            self.root = buildSegmentTree(0, len(nums) - 1, nums)

    def update(self, i: int, val: int) -> None:
        UpdateTree(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return QuerySum(self.root, i, j) 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)