// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 搜索起始位置
        l, r = 0, len(arr) - k # 这里起始点不可能大于len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            if x - arr[m] <= arr[m + k] - x:
                # case 1: x, arr[m], arr[m + k]
                # case 2: arr[m], x, arr[m+k], 想要拉大arr[m]和x之间的间距
                # move left
                r = m
            else:
                # case 1: arr[m], arr[m+k], x
                # case 2: arr[m], x, arr[m+k], 想要拉大arr[m+k]和x之间的间距
                # move right
                l = m + 1
        return arr[l:l+k]