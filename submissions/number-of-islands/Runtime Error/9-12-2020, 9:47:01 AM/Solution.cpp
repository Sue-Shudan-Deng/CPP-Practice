// https://leetcode.com/problems/number-of-islands

class Solution {
    
private:
    int row;
    int col;
    set<pair<int, int>> visited;
    vector<pair<int, int>> ds = vector<pair<int, int>>{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    void bfs(vector<vector<char>>& grid, int r, int c) {
        deque<pair<int, int>> q;
        grid[r][c] = '0';
        q.emplace_back(r, c);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto [r, c] = q.front();
                q.pop_front();
                for (auto d : ds) {
                    auto [d1, d2] = d;
                    int nr = r + d1;
                    int nc = c + d2;
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] == '1') {
                        q.emplace_back(nr, nc);
                        grid[nr][nc] = '0';
                    }
                }   
            }
        }
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        row = grid.size();
        col = grid[0].size();
        int cnt = 0;
        
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
};