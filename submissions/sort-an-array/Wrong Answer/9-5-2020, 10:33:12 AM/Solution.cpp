// https://leetcode.com/problems/sort-an-array

class Solution {
public:
    // ///////////////////
    // // Counting sort //
    // ///////////////////
    // vector<int> sortArray(vector<int>& nums) {
    //     // step1: build the counter
    //     map<int, int> counter;
    //     for (auto i : nums) counter[i]++;
    //     int k = 0;
    //     for (auto i: counter) {
    //         auto [val, freq] = i;
    //         for (int i=0; i<freq; ++i) {
    //             nums[k++] = val;
    //         }
    //     }
    //     return nums;
    // }
    
    /////////////////////////////
    // merge sort(top to down) //
    /////////////////////////////
    
    vector<int> sortArray(vector<int>& nums) {
        // step1: define merge function 
        auto merge = [] (vector<int>& nums, int start, int middle, int end) -> void {
            auto p = start;
            auto q = middle;
            vector<int> sorted_nums;
            while (p < middle && q < end) {
                if (nums[p] < nums[q]) {
                    sorted_nums.push_back(nums[p]); p++;
                } else {
                    sorted_nums.push_back(nums[q]); q++;
                }
            }
            while (p < middle) {
                sorted_nums.push_back(nums[p]); p++;
            }
            while (q < end) {
                sorted_nums.push_back(nums[q]); q++;
            }
            copy(sorted_nums.begin(), sorted_nums.end(), nums.begin()+start);
        };
        
        int step_size = 2;
        int start, middle, end = 0;
        while (step_size <= nums.size()) {
            for (int i = 0; i < nums.size(); i += step_size) {
                start = i; 
                middle = start+step_size/2;
                end = (start+step_size) < nums.size() ? (start+step_size) : nums.size();
                merge(nums, start, middle, end);
            }
            step_size *= 2;
        }
        return nums;
    }
};