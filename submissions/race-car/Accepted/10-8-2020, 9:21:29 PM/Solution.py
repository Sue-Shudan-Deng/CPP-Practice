// https://leetcode.com/problems/race-car

class Solution(object):
    def racecar(self, target):
        """
        method 1: BFS
        """
        queue = collections.deque([(0, 1, 0)])
        visited = set()
        visited.add("0_1")
        visited.add("0_-1")
        
        while queue:
            pos, speed, step = queue.popleft()
            # case 1: A
            pos1 = pos + speed
            speed1 = speed * 2
            if pos1 == target:
                return step + 1
            key1 = str(pos1) + "_" + str(speed1)
            if pos1 < 2 * target and speed1 < 2 * target and not key1 in visited:
                visited.add(key1)
                queue.append((pos1, speed1, step + 1))
            
            # case 2: R
            pos2 = pos
            speed2 = -1 if speed > 0 else 1
            key2 = str(pos2) + "_" + str(speed2)
            if not key2 in visited:
                visited.add(key2)
                queue.append((pos2, speed2, step + 1))
                
        return 0
                