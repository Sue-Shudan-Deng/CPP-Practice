// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m  = {}
        ans = []
        idx = -1
        for s in strs:
            # 注这里如果直接用sorted，那么str将会转化成list
            # 而list本身不能作为hash map的key
            # 所以可以用tuple或者转化回str
            if m.get("".join(sorted(s))) is None:
                m["".join(sorted(s))] = idx + 1
                ans.append([])
                idx += 1
            ans[m["".join(sorted(s))]].append(s)
        return ans