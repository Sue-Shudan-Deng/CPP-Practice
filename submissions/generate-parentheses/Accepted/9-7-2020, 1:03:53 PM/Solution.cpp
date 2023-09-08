// https://leetcode.com/problems/generate-parentheses

class Solution {
    
private:
    vector<string> res;    
    void backtrack(string& cur, int left, int right, int n) {
        if (left == n and right == n) {
            res.push_back(cur);
            return;
        }
        if (left > n || right > left) return;
        // set, backtrack and clear
        cur += "(";
        backtrack(cur, left + 1, right, n);
        cur.pop_back();
        
        cur += ")";
        backtrack(cur, left, right + 1, n);
        cur.pop_back();
    }
    
public:
    vector<string> generateParenthesis(int n) {
        string cur = "";
        backtrack(cur, 0, 0, n);
        return res;
    }
};