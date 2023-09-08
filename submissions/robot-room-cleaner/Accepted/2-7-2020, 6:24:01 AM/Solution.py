// https://leetcode.com/problems/robot-room-cleaner

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
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

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def bt(r = 0, c = 0, d = 0):
            robot.clean()
            visited.add((r, c))
            for i in range(4):
                new_d = (d + i) % 4 
                new_r = r + direct[new_d][0]
                new_c = c + direct[new_d][1]
                if not (new_r, new_c) in visited and robot.move():
                    bt(new_r, new_c, new_d)
                    go_back()
                robot.turnRight()
                
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        bt()