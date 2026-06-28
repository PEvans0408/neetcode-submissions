#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numset(nums.begin(), nums.end());
        if (numset.size() != nums.size()) {
            return true;
        }
        return false;
    }
};