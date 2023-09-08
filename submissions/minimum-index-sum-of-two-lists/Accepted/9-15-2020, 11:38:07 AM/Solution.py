// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {v:k for k, v in enumerate(list1)}
        m2 = {v:k for k, v in enumerate(list2)}
        ans = {}
        for k in m1.keys():
            if m2.get(k) is not None:
                ans[k] = m1[k] + m2[k]
        i = min(list(ans.values()))
        return [k for k, v in ans.items() if v == i]