// https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        counter = collections.Counter(nums)
        dp = collections.defaultdict(int)  # max value we can get with current number so far
        last, prevlast = -1, -1
        for k, num in enumerate(sorted(counter)):
            if num == last + 1:
                dp[num] = max(counter[num] * num + dp[prevlast], dp[last])
            else:
                dp[num] = counter[num] * num + dp[last]
            prevlast = last
            last = num
        return max(dp.values())