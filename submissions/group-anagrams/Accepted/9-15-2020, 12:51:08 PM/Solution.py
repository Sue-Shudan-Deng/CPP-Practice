// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            # 注这里如果直接用sorted，那么str将会转化成list
            # 而list本身不能作为hash map的key
            # 所以可以用tuple或者转化回str
            # ans[tuple(sorted(s))].append(s)
            ans["".join(sorted(s))].append(s)
        return list(ans.values())