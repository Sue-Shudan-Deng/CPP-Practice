// https://leetcode.com/problems/word-search

class Solution {
    
private:
    
    int row;
    int col;
    vector<pair<int, int>> dirs;
    bool dfs(vector<vector<char>>& board, int step, string& word, int r, int c) {
        if (step == word.size() - 1) {
            return true;
        }
        if (board[r][c] == '#') {
            return false;
        }
        board[r][c] = '#';
        for (auto ds : dirs) {
            auto [dr, dc] = ds;
            auto new_r = r + dr; 
            auto new_c = c + dc;
            if (new_r >= 0 && new_r < row && new_c >= 0 && new_c < col) {
                if (board[new_r][new_c] == word[step + 1] && dfs(board, step + 1, word, new_r, new_c)) {
                    return true;
                }
            }
        }
        board[r][c] = word[step];
        return false;
    }
    
public:
    bool exist(vector<vector<char>>& board, string word) {
        row = board.size();
        col = board[0].size();
        dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (board[r][c] == word[0] && dfs(board, 0, word, r, c)) {
                    return true;
                }
            }
        }
        return false;
    }
};