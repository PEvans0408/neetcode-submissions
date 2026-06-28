class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            int pointer1 = nums[i];
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    int pointer2 = nums[j];
                    if (pointer1 + pointer2 == target) {
                        vector<int> solution = {i, j};
                        return solution;
                    }
                }
                continue;
            }
        }
    };
};
