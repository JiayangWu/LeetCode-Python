class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            int temp = target - nums[i];
            if (m.count(temp)){
                res.push_back(m[temp]);
                res.push_back(i);
                break;
            }
             m[nums[i]] = i; 
        }
       return res; 
    }
};