// https://leetcode.com/problems/random-pick-with-weight

class Solution:
    """
    https://www.youtube.com/watch?v=nlJ8XSIWLvo
    cdf + bianry search  
    """
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.prefix = [0 for _ in range(self.n)]
        self.prefix[0] = w[0]
        for i in range(1, self.n):
            self.prefix[i] = self.prefix[i-1] + w[i]

    def pickIndex(self) -> int:
        p = random.randint(1, self.prefix[-1])
        l, r = 0, self.n - 1
        while l < r:
            m = l + (r - l) // 2
            if self.prefix[m] >= p:
                r = m
            else:
                l = m + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()