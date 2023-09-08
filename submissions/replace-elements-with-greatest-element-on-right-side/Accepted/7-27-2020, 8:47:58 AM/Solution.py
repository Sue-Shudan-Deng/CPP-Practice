// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], prev_max = prev_max, max(prev_max, arr[i])
        return arr