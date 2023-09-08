// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s;
        s.push(-1);
        int n = heights.size(), ans = 0;
        for (int i = 0; i < n; ++i) {
            while (s.top() != -1 && heights[s.top()] > heights[i]) {
                int h = heights[s.top()];
                int area = h * (i - s.top() - 1);
                ans = max(ans, area);
            }
            s.push(i);
        }
        while (s.top() != -1) {
            int h = heights[s.top()];
            int area = h * (n - s.top() - 1);
            ans = max(ans, area);
        }
        return ans;
    }
};