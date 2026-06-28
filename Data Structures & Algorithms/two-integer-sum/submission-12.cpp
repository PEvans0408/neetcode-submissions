class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        for (int idx = 0; idx < nums.size(); idx++) {
            if (auto it = hashmap.find(target - nums[idx]); it != hashmap.end()) {
                return {it->second, idx};
            }
            else {
                hashmap.emplace(nums[idx], idx);
            }   
        }
        return {};
    }
};
