// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int row = matrix.size(), col = matrix[0].size();
        int r = row - 1, c = 0; // starting point 
        
        while (r > 0 && c < col - 1) {
            while (matrix[r][c] > target) r--;
            while (matrix[r][c] < target) c++;
            if (matrix[r][c] == target) return true;
        }
        return false;
    }
};