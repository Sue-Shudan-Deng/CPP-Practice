// https://leetcode.com/problems/expressive-words

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        s_counter = collections.Counter(S)
        res  = 0
        for w in words:
            w_counter = collections.Counter(w)
            if set(s_counter.keys()) == set(w_counter.keys()) and all(char in s_counter and (s_counter[char] == w_counter[char] or s_counter[char] >= 3) for char in w_counter):
                res += 1
        return res