// https://leetcode.com/problems/open-the-lock

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 生成一个generator
        def neighbors(node: str):
            for i in range(4):
                for d in (-1, 1):
                    x = (int(node[i]) + d) % 10
                    yield node[:i] + str(x) + node[i+1:]
        
        queue = deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deadends:
                continue
            for n in neighbors(node):
                if n not in visited:
                    visited.add(n)
                    queue.append((n, depth+1))
        return -1