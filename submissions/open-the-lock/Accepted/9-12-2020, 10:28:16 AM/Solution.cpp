// https://leetcode.com/problems/open-the-lock

class Solution {
    
private:
    int row;
    int col;
    set<string> visited;
    set<string> dead;
    deque<pair<string, int>> q;
    
public:
    int openLock(vector<string>& deadends, string target) {
        if (deadends.empty()) return -1;
        string start = "0000";
        dead = set<string>(deadends.begin(), deadends.end());
        if (dead.find(start) != dead.end()) {
            return -1;
        }
        string cur, next;
        auto plus = [](string num, int index) -> string {
            num[index] = (num[index] - '0' + 1) % 10 + '0';
            return num;
        };
        auto minus = [](string num, int index) -> string {
            num[index] = (num[index] - '0' + 9) % 10 + '0';
            return num;
        };
        
        int cnt = 0;
        q.emplace_back(start, cnt);
        while (!q.empty()) {
            auto [cur, cnt] = q.front();
            q.pop_front();
            if (cur == target) {
                return cnt;
            }
            for (int i = 0; i < 4; ++i) {
                next = plus(cur, i);
                if (visited.find(next) == visited.end() && 
                    dead.find(next) == dead.end()) {
                    visited.insert(next);
                    q.emplace_back(next, cnt + 1);
                }
                next = minus(cur, i);
                if (visited.find(next) == visited.end() &&
                    dead.find(next) == dead.end()) {
                    visited.insert(next);
                    q.emplace_back(next, cnt + 1);
                }
            }
        }
        return -1;
    }
};