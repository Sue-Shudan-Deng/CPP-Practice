// https://leetcode.com/problems/sudoku-solver

class Solution {

private:
    vector<vector<int>> row;
    vector<vector<int>> col;
    vector<vector<int>> box;
    
    void updateBoard(vector<vector<char>>& board, int i, int j, int ch, int sign) {
        row[i][ch] = sign;
        col[j][ch] = sign;
        int n = (i / 3) * 3 + j / 3;
        box[n][ch] = sign;
        board[i][j] = sign ? ch + '0' : '.';
    }
    
    
    bool available(int i, int j, int ch) {
        int n = (i / 3) * 3 + j / 3;
        return !row[i][ch] && !col[j][ch] && !box[n][ch];
    }
    
    bool backtrack(vector<vector<char>>& board, int i, int j) {
        if (i > 8) return true;
        
        int ni = j == 8 ? i + 1 : i;
        int nj = j == 8 ? 0 : j + 1;
        
        if (board[i][j] != '.') return backtrack(board, ni, nj); // directly go to next cell 
        
        // for all possible ints
        for (int ch = 1; ch < 10; ++ch) {
            if (available(i, j, ch)) {
                updateBoard(board, i, j, ch, 1);
                if (backtrack(board, ni, nj)) return true; // force to quit
                updateBoard(board, i, j, ch, 0);
            }
        }
        return false;  // doesn't mean anything: just to quit the function
    }
    
    
public:
    void solveSudoku(vector<vector<char>>& board) {
        // loop over the matrix
        // for which row, if a char is there, put 1. The same for column and box
        row = vector<vector<int>>(9, vector<int>(10, 0));
        col = vector<vector<int>>(9, vector<int>(10, 0));
        box = vector<vector<int>>(9, vector<int>(10, 0));
        
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int ch = board[i][j] - '0';
                    int n = (i / 3) * 3 + j / 3;
                    row[i][ch] = 1;
                    col[j][ch] = 1;
                    box[n][ch] = 1;
                }
            }
        }
        backtrack(board, 0, 0);
    }
};