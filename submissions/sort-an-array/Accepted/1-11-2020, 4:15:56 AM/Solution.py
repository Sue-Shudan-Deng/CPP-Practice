// https://leetcode.com/problems/sort-an-array

class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Count sort，赖皮
    #     """
    #     C, m, M, S = collections.Counter(nums), min(nums), max(nums), []
    #     for n in range(m, M+1):
    #         S.extend([n]*C[n])
    #     return S
    
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Bottom-up mergesort
        """
        def merge(l1: List[int], l2: List[int]) -> List[int]:
            res = []
            left_cursor = 0
            right_cursor = 0
            while left_cursor < len(l1) and right_cursor < len(l2):
                if l1[left_cursor] < l2[right_cursor]:
                    res.append(l1[left_cursor])
                    left_cursor += 1
                else:
                    res.append(l2[right_cursor])
                    right_cursor += 1
            res.extend(l1[left_cursor:])
            res.extend(l2[right_cursor:])
            return res
            
        size = 1
        while size < len(nums):
            size += size
            for pos in range(0, len(nums), size):  # 这一步的想法是关键
                start = pos
                mid = pos + size // 2
                end = pos + size
                nums[start:end] = merge(nums[start:mid], nums[mid:end])
        return nums
                