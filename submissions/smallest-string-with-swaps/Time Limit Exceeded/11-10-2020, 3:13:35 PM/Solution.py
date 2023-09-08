// https://leetcode.com/problems/smallest-string-with-swaps

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        queue = collections.deque([s])
        ans = s
        visited = set()
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            ans = min(ans, cur) 
            for i, j in pairs:
                queue.append(cur[:i] + cur[j] + cur[i+1:j] + cur[i] + cur[j+1:])
        return ans