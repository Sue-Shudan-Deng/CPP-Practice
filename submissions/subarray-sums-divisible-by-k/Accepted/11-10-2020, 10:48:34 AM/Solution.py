// https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        居然是560的变形，这真是完全想不到
        """
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        cur, cnt = 0, 0
        for num in A:
            cur = (num + cur) % K
            cnt += prefix[cur] # backward until index -1
            prefix[cur] += 1
            
        return cnt