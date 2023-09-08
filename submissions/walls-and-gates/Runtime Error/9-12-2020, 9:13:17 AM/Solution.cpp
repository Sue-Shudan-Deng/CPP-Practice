// https://leetcode.com/problems/walls-and-gates

class Solution {
    
// 模板是什么？能不能用visited? 能不能提前退出？
// template 2, not, no
    
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int row = rooms.size();
        int col = rooms[0].size();
        deque<pair<int, int>> q;
        vector<pair<int, int>> ds = vector<pair<int, int>>{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int cur = 0;
        
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (rooms[r][c] == 0) {
                    q.emplace_back(r, c);
                }
            }
        }
        
        while (!q.empty()) {
            ++cur;
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto [r, c] = q.front();
                cout << r << " " << c << endl;
                q.pop_front();
                for (auto j : ds) {
                    auto [d1, d2] = j;
                    int nr = r + d1;
                    int nc = c + d2;
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && rooms[nr][nc] == INT_MAX) {
                        rooms[nr][nc] = cur;
                        q.emplace_back(nr, nc);
                    }
                }
            }   
        }
    }
};