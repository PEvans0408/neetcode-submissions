class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> retvect;
        sort(nums.begin(), nums.end());
        for (int pointer1 = 0; pointer1 < nums.size(); pointer1++) {
            if (pointer1 > 0 && nums[pointer1] == nums[pointer1 - 1]) {
                continue;
            }
            int pointer2 = pointer1 + 1;
            int pointer3 = nums.size() - 1;
            while (pointer2 < pointer3) {
                int target = -nums[pointer1];
                int sum = nums[pointer2] + nums[pointer3];
                if (sum < target) {
                    pointer2++;
                }
                else if (sum > target) {
                    pointer3--;
                }
                else {
                    retvect.push_back({nums[pointer1], nums[pointer2], nums[pointer3]});
                    pointer2++;
                    pointer3--;
                    while (pointer2 < pointer3 && nums[pointer2] == nums[pointer2 - 1]) {
                        pointer2++;}
                    while (pointer2 < pointer3 && nums[pointer3] == nums[pointer3 + 1]) {
                        pointer3--;}
                }
            }
        }
        return retvect;
    }
};
