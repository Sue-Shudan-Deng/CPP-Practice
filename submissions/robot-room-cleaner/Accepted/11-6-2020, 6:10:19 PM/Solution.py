// https://leetcode.com/problems/robot-room-cleaner

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    
    def goback(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()        

    def cleanRoom(self, robot):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def dfs(r, c, d):
            if (r, c) in visited:
                return
            visited.add((r, c))
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                new_r, new_c = r + dirs[new_d][0], c + dirs[new_d][1]
                avaliable = robot.move()
                if avaliable:
                    dfs(new_r, new_c, new_d)
                    self.goback(robot)
                robot.turnRight()
        
        dfs(0, 0, 0)