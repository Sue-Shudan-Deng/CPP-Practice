// https://leetcode.com/problems/kth-largest-element-in-a-stream

# class Node:
#     def __init__(self, val: int, cnt: int):
#         self.val = val
#         self.cnt = cnt
#         self.left = None
#         self.right = None
        
# def insertNode(root: Node, num: int):
#     if not root:
#         return Node(num, 1)
#     if num < root.val:
#         root.left = insertNode(root.left, num)
#     else:
#         root.right = insertNode(root.right, num)
#     root.cnt += 1
#     return root
        
# def searchKth(root: Node, k: int):
#     m = 0 if not root.right else root.right.cnt
#     if k == m+1:
#         return root.val
#     elif k <= m:
#         # 可以在右边搜
#         return searchKth(root.right, k)
#     else:
#         # 只能在左边搜
#         return searchKth(root.left, k-m-1)

class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.root = None
#         for n in nums:
#             self.root = insertNode(self.root, n)
#         self.size = k

#     def add(self, val: int) -> int:
#         self.root = insertNode(self.root, val)
#         return searchKth(self.root, self.size)

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        for n in nums[:k]:
            heappush(self.h, n)
        for n in nums[k:]:
            heappushpop(self.h, n)
        print(self.h)

    def add(self, val: int) -> int:
        heappushpop(self.h, val)
        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)