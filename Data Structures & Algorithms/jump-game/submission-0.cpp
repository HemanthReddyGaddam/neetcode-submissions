class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        vector<int> dp(n,0);
        dp[0]=1;
        for(int i=0;i<n;i++){
            if(!dp[i]){
                return false;
            }
            int temp=nums[i];
            int j=1;
            while(temp && i+j<n){
                dp[i+j]=1;
                j++;
                temp--;
            }
        }
        return dp[n-1]==1 ? true : false;
        
    }
};
