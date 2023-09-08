// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s;
        s.push(-1);
        int n = heights.size(), ans = 0;
        for (int i = 0; i < n; ++i) {
            while (s.top() != -1 && heights[s.top()] > heights[i]) {
                int j = s.top();
                s.pop();
                int h = heights[j] * (i - j);
                ans = max(ans, h);
            }
            s.push(i);
        }
        while (s.top() != -1) {
            int j = s.top();
            s.pop();
            int h = heights[j] * (n - j);
            ans = max(ans, h);
        }
        return ans;
    }
};