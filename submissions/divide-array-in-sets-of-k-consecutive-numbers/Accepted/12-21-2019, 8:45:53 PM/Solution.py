// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

import collections
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        print(nums)
        if nums == []:
            return True
        if len(nums) % k:
            return False
        else:
            cnt = collections.Counter(nums)
            while (len(cnt) > 0):
                x = min(cnt)
                x_cnt = cnt[x]
                for v in range(x, x+k):
                    print(v)
                    if cnt[v] < x_cnt:
                        return False 
                    elif cnt[v] == x_cnt:
                        cnt.pop(v)
                    else:
                        cnt[v] -= x_cnt
                # print("cnt:", cnt)
            return True