// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Counting sort，赖皮
        """
        C, m, M, S = collections.Counter(nums), min(nums), max(nums), []
        for n in range(m, M+1):
            S.extend([n]*C[n])
        return S
    
class Solution:
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
              
class Solution:        
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        quick sort
        """
        n = len(nums)
        self.qsort(nums, 0, n - 1) # 一定要注意，python是按引用传递的，不是按值传递，因此nums的值会修改
        return nums

    def qsort(self, lst, lo, hi):
        """
        Helper
        :param lst: the list to sort
        :param lo:  the index of the first element in the list
        :param hi:  the index of the last element in the list
        :return: the sorted list
        """
        if lo < hi:
            p = self.partition(lst, lo, hi)
            # print(lst, hi, p)
            self.qsort(lst, lo, p - 1)
            # print(lst, hi)
            self.qsort(lst, p + 1, hi)

    # def partition(self, lst, lo, hi):
    #     """
    #     Picks the last element hi as a pivot
    #     and returns the index of pivot value in the sorted array
    #     注：这里的partition算法是单向版本
    #     """
    #     pivot = lst[hi]
    #     i = lo
    #     for j in range(lo, hi):
    #         if lst[j] < pivot:
    #             lst[i], lst[j] = lst[j], lst[i]
    #             i += 1
    #     lst[i], lst[hi] = lst[hi], lst[i]
    #     return i
    
    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            # If the current value we're looking at is larger than the pivot
            # it's in the right place (right side of pivot) and we can move left,
            # to the next element.
            # We also need to make sure we haven't surpassed the low pointer, since that
            # indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[high] >= pivot:
                high = high - 1

            # Opposite process of the one above
            while low <= high and array[low] <= pivot:
                low = low + 1

            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
            if low <= high:
                array[low], array[high] = array[high], array[low]
                # The loop continues
            else:
                # We exit out of the loop
                break

        array[start], array[high] = array[high], array[start]

        return high