// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # step 1, binary search, insert the new interval to the original intervals
        l, r = 0, len(intervals)
        while l < r:
            m = l + (r - l) // 2
            if intervals[m][0] >= newInterval[0]:
                r = m
            else:
                l = m + 1
        # insertion point: l
        intervals = intervals[:l] + [newInterval] + intervals[l:]
        
        # step 2, merge intervals
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = i[1]
        return merged