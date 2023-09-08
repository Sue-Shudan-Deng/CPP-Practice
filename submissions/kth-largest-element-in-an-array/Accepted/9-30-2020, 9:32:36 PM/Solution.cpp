// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // priority_queue<int, vector<int>, less<int>> pq; // maxheap
        // int n = nums.size();
        // for (auto n : nums) {
        //     pq.push(n);
        // }
        // for (int i = n - 1; i > n - k; --i) {
        //     pq.pop();
        // }
        // return pq.top();
        
        priority_queue<int, vector<int>, greater<int>> pq; // minheap
        int n = nums.size();
        for (auto n : nums) {
            pq.push(n);
            if (pq.size() > k) {
                pq.pop();
            }
        }
        return pq.top();
    }
};