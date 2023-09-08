// https://leetcode.com/problems/next-closest-time

class Solution {
public:
    string nextClosestTime(string time) {
        int hour = stoi(time.substr(0, 2));
        int minute = stoi(time.substr(3, 2));
        int cur = hour * 60 + minute;
        int total = 24 * 60;
        set<int> s{hour / 10, hour % 10, minute / 10, minute % 10};
        
        while (true) {
            cur = (cur + 1) % total;
            int x1 = cur / 60 / 10;
            int x2 = cur / 60 % 10;
            int x3 = cur % 60 / 10;
            int x4 = cur % 60 % 10;
            if (s.count(x1) && s.count(x2) && s.count(x3) && s.count(x4)) {
                return to_string(x1) + to_string(x2) + ":" + to_string(x3) + to_string(x4); 
            }
        }
    }
};