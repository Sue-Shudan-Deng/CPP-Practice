// https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans, visited = [], set()
        def dfs(start, cur):
            n = len(S)

            while start < n and S[start].isnumeric():
                cur += S[start]
                start += 1
                
            if start < n:
                dfs(start + 1, cur + S[start].upper())
                dfs(start + 1, cur + S[start].lower())
            else:
                ans.append(cur)
                
        dfs(0, "")
        return ans