// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        ans = []
        for k, v in counter1.items():
            if counter2.get(k) is not None:
                ans.extend([k] * min(v, counter2[k]))
        return ans