// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {v:k for k, v in enumerate(list1)}
        m2 = {v:k for k, v in enumerate(list2)}
        cnt = float("inf")
        ans = []
        for k in m1.keys():
            if m2.get(k):
                if m1[k] + m2[k] < cnt:
                    ans = [k]
        return ans