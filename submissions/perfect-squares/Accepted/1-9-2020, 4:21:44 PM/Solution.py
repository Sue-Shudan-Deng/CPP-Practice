// https://leetcode.com/problems/perfect-squares

from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squarenums = [i*i for i in range(1, int(n**0.5) + 1)]
        queue = deque([(n, 0)])
        while queue:
            curr, level = queue.popleft()
            for num in list(filter(lambda x: x<=curr, squarenums)):
                if curr == num:
                    return level+1
                else:
                    queue.append((curr-num, level+1))
        return level