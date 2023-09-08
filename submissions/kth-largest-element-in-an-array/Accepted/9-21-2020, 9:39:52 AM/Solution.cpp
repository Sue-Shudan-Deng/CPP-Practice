// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, less<int>> pq;
        int n = nums.size();
        for (auto n : nums) {
            pq.push(n);
        }
        for (int i = n - 1; i > n - k; --i) {
            pq.pop();
        }
        return pq.top();
    }
};