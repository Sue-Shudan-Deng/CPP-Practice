// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution {
    
private:
    vector<string> v;
    vector<string> ret;
    void backtrack(string& digits, string& cur) {
        if (digits != "" && cur.size() == digits.size()) {
            ret.push_back(cur);
            return;
        }
        
        string s = v[digits[cur.size()] - '0'];
        for (auto c : s) {
            cur.push_back(c);
            backtrack(digits, cur);
            cur.pop_back();
        }
    }
    
public:
    vector<string> letterCombinations(string digits) {
        v = vector<string>{"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        string cur = "";
        backtrack(digits, cur);
        return ret;
    }
};