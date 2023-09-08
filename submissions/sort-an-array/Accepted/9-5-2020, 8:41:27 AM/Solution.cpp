// https://leetcode.com/problems/sort-an-array

class Solution {
public:
    ///////////////////
    // Counting sort //
    ///////////////////
    vector<int> sortArray(vector<int>& nums) {
        // step1: build the counter
        map<int, int> counter;
        for (auto i : nums) counter[i]++;
        int k = 0;
        for (auto i: counter) {
            auto [val, freq] = i;
            for (int i=0; i<freq; ++i) {
                nums[k++] = val;
            }
        }
        return nums;
    }
};