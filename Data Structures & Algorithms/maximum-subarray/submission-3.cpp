class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxsum=INT_MIN;
        int currentsum=0;
        for(auto it : nums){
            currentsum=max(currentsum+it,it);
            maxsum=max(maxsum,currentsum);
        }
        return maxsum;
    }
};