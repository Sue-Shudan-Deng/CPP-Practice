// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 搜索起始位置
        l, r = 0, len(arr) - k # 这里起始点不可能大于len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            if x - arr[m] <= arr[m + k] - x:
                # move left
                r = m
            else:
                # move right
                l = m + 1
        return arr[l:l+k]