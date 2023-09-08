// https://leetcode.com/problems/sort-an-array

class Solution {
////////////////////
// insertion sort //
////////////////////
public:
    vector<int> sortArray(vector<int>& nums) {
        for (int i=1; i<nums.size(); ++i) {
            int key = nums[i];
            int j = i-1;
            while (j >= 0 && key < nums[j]) {
                nums[j+1] = nums[j];
                j--;
            }
            nums[j+1] = key;
        }
        return nums;
    }
};



// class Solution {
// public:
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
    
    // ///////////////////////////
    // // merge sort(botton up) //
    // ///////////////////////////
    
//     vector<int> sortArray(vector<int>& nums) {
//         // step1: define merge function 
//         auto merge = [] (vector<int>& nums, int start, int middle, int end) -> void {
//             auto p = start;
//             auto q = middle;
//             vector<int> sorted_nums;
//             while (p < middle && q < end) {
//                 if (nums[p] < nums[q]) {
//                     sorted_nums.push_back(nums[p]); p++;
//                 } else {
//                     sorted_nums.push_back(nums[q]); q++;
//                 }
//             }
//             while (p < middle) {
//                 sorted_nums.push_back(nums[p]); p++;
//             }
//             while (q < end) {
//                 sorted_nums.push_back(nums[q]); q++;
//             }
//             copy(sorted_nums.begin(), sorted_nums.end(), nums.begin()+start);
//         };
        
//         int step_size = 2;
//         int start, middle, end = 0;
//         while (step_size < nums.size() * 2) {
//             for (int i = 0; i < nums.size(); i += step_size) {
//                 start = i; 
//                 middle = start + step_size/2;
//                 end = (start + step_size) < nums.size() ? (start + step_size) : nums.size();
//                 merge(nums, start, middle, end);
//                 // cout << start << " " << middle << " " << end << endl;
//             }
//             step_size *= 2;
//         }
//         return nums;
//     }
// };
// class Solution {
//     ////////////////
//     // quick sort //
//     ////////////////
// private:
//     int partition(vector<int>& nums, int lo, int hi) {
//         int pivot = lo;
//         lo++;
//         while (true) {
//             while (lo <= hi && nums[lo] <= nums[pivot]) lo++;
//             while (lo <= hi && nums[hi] >= nums[pivot]) hi--;
//             if (lo <= hi) {
//                 swap(nums[lo], nums[hi]); // 说明两边都遇到瓶颈了，交换即可
//             } else {
//                 break;
//             }
//         }
//         swap(nums[pivot], nums[hi]);
//         return hi;
//     }
    
//     void qsort(vector<int>& nums, int l, int r) {
//         if (l >= r) return;   
//         int p = partition(nums, l, r);
//         qsort(nums, l, p-1);
//         qsort(nums, p+1, r);
//     }
        
// public:
//     vector<int> sortArray(vector<int>& nums) {
//         qsort(nums, 0, nums.size()-1);
//         return nums;
//     }
// };