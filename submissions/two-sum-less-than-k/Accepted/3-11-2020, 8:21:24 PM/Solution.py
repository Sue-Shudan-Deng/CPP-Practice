// https://leetcode.com/problems/two-sum-less-than-k

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        ans = float("-inf")
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] + A[j] < K:
                ans = max(ans, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return ans if ans != float("-inf") else -1