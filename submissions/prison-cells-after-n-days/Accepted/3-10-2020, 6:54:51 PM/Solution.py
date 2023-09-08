// https://leetcode.com/problems/prison-cells-after-n-days

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        这道题的写法真的太妙了，需要认真学习
        """
        def nextday(cells: list) -> list:
            return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1]) for i in range(len(cells))]
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= (seen[c] - N)
            seen[c] = N
            
            if N >= 1:
                N -= 1
                cells = nextday(cells)
                
        return cells