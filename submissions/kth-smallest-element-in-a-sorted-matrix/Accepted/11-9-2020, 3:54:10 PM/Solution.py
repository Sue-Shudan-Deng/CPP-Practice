// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        """
        bisect牛逼！！！
        """
        
        # def upper_bound(row, k):
        #     l, r = 0, len(row)
        #     while l < r:
        #         m = l + (r - l) // 2
        #         if row[m] > k:
        #             r = m
        #         else:
        #             l = m + 1
        #     """
        #     本应该return下标l - 1，但要计算个数，所以还是l
        #     """
        #     return l
        
        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)
        while l < r:
            m = l + (r - l) // 2
            total = 0
            for row in matrix:
                # total += upper_bound(row, m)
                total += bisect.bisect(row, m)
            """
            注意这里之所以选择upper bound是因为需要包含m
            """
            if total >= k:
                r = m
            else:
                l = m + 1
        return l