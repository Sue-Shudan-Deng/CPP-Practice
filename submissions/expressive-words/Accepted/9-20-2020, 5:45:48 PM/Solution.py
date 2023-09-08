// https://leetcode.com/problems/expressive-words

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # 我跟正确答案的区别是我之前用的是counter，但标答用的是RLE, 
        # 但正好这里不能用counter因为要考虑顺序性
        # 这道题具有非常强的特殊性，需要重点记忆
        def RunningLengthEncoding(s):
            return zip(*[(k, len(list(group))) for k, group in itertools.groupby(s)])
        ans = 0
        if s == "":
            return ans
        s_char, s_count = RunningLengthEncoding(s)
        for w in words:
            w_char, w_count = RunningLengthEncoding(w)
            if s_char != w_char:
                continue
            ans += all((c1 == c2) or (c1 > c2 and c1 >= 3) for c1, c2 in zip(s_count, w_count))
        return ans