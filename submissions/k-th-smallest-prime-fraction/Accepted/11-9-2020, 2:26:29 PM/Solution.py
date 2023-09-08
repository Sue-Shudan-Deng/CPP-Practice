// https://leetcode.com/problems/k-th-smallest-prime-fraction

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def count_lower(x):
            l, cnt, n = 0, 0, len(A)
            best = [0, n - 1]
            for r in range(l+1, n):
                while l < r and (A[l] / A[r]) < x:
                    l += 1
                cnt += l
                if l > 0:
                    best = max(best, [l-1, r], key=lambda x: A[x[0]] / A[x[1]])
            return cnt, best
        
        l, r, n = 0, 1, len(A)
        ans = [0, n - 1]
        while l < r - 1e-9:
            m = l + (r - l) / 2
            cnt, best = count_lower(m)
            if cnt >= K:
                ans = best
                r = m
            else:
                l = m
            
        return [A[ans[0]], A[ans[1]]]