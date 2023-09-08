// https://leetcode.com/problems/meeting-rooms

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto x, auto y) {return x[0] < y[0];});
        int n = intervals.size();
        if (n <= 1) {
            return true;
        }
        for (int i = 1; i < n; ++i) {
            if (intervals[i][0] < intervals[i-1][1]) {
                return false;
            }
        }
        return true;
    }
};