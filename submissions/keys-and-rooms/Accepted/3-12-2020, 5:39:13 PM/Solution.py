// https://leetcode.com/problems/keys-and-rooms

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False for _ in range(len(rooms))]
        seen[0], stack = True, [0]
        while stack:
            n = stack.pop()
            for nei in rooms[n]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)