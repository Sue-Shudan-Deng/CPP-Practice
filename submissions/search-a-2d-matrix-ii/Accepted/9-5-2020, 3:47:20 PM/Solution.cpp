// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        int row = matrix.size(), col = matrix[0].size();
        int r = row - 1, c = 0; // starting point 
        while (r >= 0 && c <= col-1) {
            if (matrix[r][c] > target) r--;
            else if (matrix[r][c] < target) c++;
            else return true;
        }
        return false;
    }
};