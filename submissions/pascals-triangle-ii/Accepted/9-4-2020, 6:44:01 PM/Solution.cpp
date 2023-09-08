// https://leetcode.com/problems/pascals-triangle-ii

// 1
// 1 1
// 1 2 1
// 1 3 3 1
// 1 4 6 4 1

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ret(rowIndex+1);
        transform(ret.begin(), ret.end(), ret.begin(), [](int i) -> int{return i+1;});
        // rowIndex = 2
        for (int i = 0; i < rowIndex-1; i++) {
            for (int j = i; j > -1; j--) {
                ret[j+1] = ret[j+1] + ret[j];
            }
        }
        return ret;
    }
};