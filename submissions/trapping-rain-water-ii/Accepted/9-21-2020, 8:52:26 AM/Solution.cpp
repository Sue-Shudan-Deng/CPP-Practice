// https://leetcode.com/problems/trapping-rain-water-ii

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        int row = heightMap.size(), col = heightMap[0].size();
        vector<vector<int>> visited(row, vector<int>(col, 0));
        vector<pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int ans = 0;
        
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (i == 0 || i == row-1 || j == 0 || j == col-1) {
                    visited[i][j] = 1;
                    pq.emplace(heightMap[i][j], i, j);
                }
            }
        }
        
        while (!pq.empty()) {
            auto [val, r, c] = pq.top();
            pq.pop();
            for (auto ds : dirs) {
                auto [dr, dc] = ds;
                int new_r = r + dr;
                int new_c = c + dc;
                if (0 <= new_r && new_r < row && 0 <= new_c && new_c < col && !visited[new_r][new_c]) {
                    visited[new_r][new_c] = 1;
                    ans += max(0, heightMap[r][c] - heightMap[new_r][new_c]);
                    heightMap[new_r][new_c] = max(heightMap[r][c], heightMap[new_r][new_c]);
                    pq.emplace(heightMap[new_r][new_c], new_r, new_c);
                }
            }
        }
        return ans;
    }
};