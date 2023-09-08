// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s; // -1 serve as a guard since no element (height) can be negative
        s.push(-1);
        int n = heights.size();
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            // if s is not empty and the element which is currently
            // visited is smaller than the stack top
            while (s.top() != -1 && heights[i] < heights[s.top()]) {
                // pop the stack top
                int cur = s.top();
                s.pop();
                int r = i;
                int l = cur; 
                ret = max(ret, heights[cur] * (r - l));
            }
            s.push(i);
        }
        
        // at the end, usually 1 or 2 elements left
        while (s.top() != -1) {
            int cur = s.top();
            s.pop();
            int r = n; // at the end
            int l = cur; 
            ret = max(ret, heights[cur] * (r - l));
        }
        return ret;
    }
};