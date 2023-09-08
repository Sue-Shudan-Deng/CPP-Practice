// https://leetcode.com/problems/keys-and-rooms

class Solution {
    
private:
    vector<bool> visited;
    void dfs(vector<vector<int>>& rooms, int cur_roomnum) {
        if (visited[cur_roomnum]) {
            return;
        }
        visited[cur_roomnum] = true;
        for (auto nxt_roomnum : rooms[cur_roomnum]) {
            dfs(rooms, nxt_roomnum);
        }
    }
    
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        visited = vector<bool>(n, false);
        dfs(rooms, 0);
        for (auto i : visited) {
            if (!visited[i]) {
                return false;
            }
        }
        return true;
    }
};