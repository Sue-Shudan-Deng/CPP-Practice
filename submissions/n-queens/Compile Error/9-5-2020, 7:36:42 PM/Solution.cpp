// https://leetcode.com/problems/n-queens

class Solution {
    
private:
    vector<vector<string>> sol_;
    vector<string> board;
    vector<int> row_;
    vector<int> diag1_;
    vector<int> diag2_;
    int size;
    
    bool available(int r, int c) {
        return !row_[r] && !diag1_[r+c] && !diag2_[r-c+size-1];
    }
    
    void updateBoard(int r, int c, int set) {
        row_[r] = set;
        diag1_[r+c] = set;
        diag2_[r-c+size-1] = set;
        board[r][c] = set ? 'Q' : '.';
    }
    
    void nQueens(int c) {
        if (c == size) {
            sol_.push_back(board);
            return;
        }
        
        for (int r = 0; r < size; ++r) {
            if (!available(r, c)) continue;
            updateBoard(r, c, 1);
            nQueens(c+1);
            updateBoard(r, c, 0);
        }
    }
    
public:
    int totalNQueens(int n) {
        row_ = vector<int>(n, 0);
        diag1_ = vector<int>(2*n-1, 0);
        diag2_ = vector<int>(2*n-1, 0);
        board = vector<string>(n, string(n, '.'));
        size = n;
        
        nQueens(0);
        return sol_;
    }
};