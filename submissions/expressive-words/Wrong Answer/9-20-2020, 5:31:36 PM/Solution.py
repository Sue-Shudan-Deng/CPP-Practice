// https://leetcode.com/problems/expressive-words

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for w in words:
            i, j = 0, 0
            n1, n2 = len(s), len(w)
            if n1 < n2:
                continue
            while i < n1 and j < n2:
                if s[i] != w[j]:
                    break
                cnt = 0
                while i < n1 and j < n2 and s[i] == w[j]:
                    i += 1
                    j += 1
                    cnt += 1
                if j == n2:
                    if i == n1 or s[i] != w[j-1]:
                        break
                else:
                    if w[j] == w[j-1] and s[i] != w[j-1]:
                        break
                while i < n1 and s[i] == w[j-1]:
                    i += 1
                    cnt += 1
                if cnt < 3:
                    break
            if i == n1 and j == n2 and cnt >= 3:
                res += 1
        return res