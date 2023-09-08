// https://leetcode.com/problems/contains-duplicate-iii

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k==0) {
            return false;
        }
        set<long long> s; // maintain a sorted hashset of size at most k
        for(int i = 0; i < nums.size(); ++i){
            long long val = nums[i];
            if(!s.empty()){
                if (s.size() == k + 1) {
                    s.erase(nums[i-k-1]);
                }
                auto higher = s.lower_bound(val);
                // cout << "set: ";
                // for (auto i : s) cout << i << " ";
                // cout << endl;
                // cout << "higher: " << *higher << " val: " << val << endl;
                // cout << (higher == s.end()) << endl;
                //higher points to smallest element bigger or equal to val
                if (higher != s.end() && (*higher - val <= t)) {
                    return true;
                }
                if (higher != s.begin()) {
                    auto lower = --higher;
                    // cout << "set: ";
                    // for (auto i : s) cout << i << " ";
                    // cout << endl;
                    // cout << "lower: " << *lower << " val: " << val << endl;
                    //now lower should point to biggest element smaller than val
                    if (lower != s.end() && ((val - *lower) <= t)) {
                        return true;
                    }
                }
            }
            s.insert(val);
        }
        return false;
    }
};