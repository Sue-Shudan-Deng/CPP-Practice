// https://leetcode.com/problems/robot-room-cleaner

/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
    
private:
    vector<pair<int, int>> ds;
    void goback(Robot& robot) {
        robot.turnLeft();
        robot.turnLeft();
        robot.move();
        robot.turnLeft();
        robot.turnLeft();
    }   
    
    void backtrack(Robot& robot, pair<int, int> cur_cell, int cur_dir, 
                   set<pair<int, int>>& visited) {
        
        if (find(visited.begin(), visited.end(), cur_cell) != visited.end()) return;
        robot.clean();
        visited.insert(cur_cell);
        for (int i = 0; i < 4; ++i) {
            // set
            bool available = robot.move();
            if (available) {
                // Then backtrack(and clear)
                int new_dir = (cur_dir + i) % 4;
                pair<int, int> new_cell{cur_cell.first + ds[new_dir].first, 
                                        cur_cell.second + ds[new_dir].second};
                backtrack(robot, new_cell, new_dir, visited);
                // clear
                goback(robot);
            }
            robot.turnLeft();
        }
    }
    
public:
    void cleanRoom(Robot& robot) {
        ds = vector<pair<int, int>>{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        set<pair<int, int>> visited;
        backtrack(robot, pair<int, int>{0, 0}, 0, visited);
    }
};