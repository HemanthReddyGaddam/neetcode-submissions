class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int l=0,r=0;
        int n=s.size();
        vector<bool> dp(n,false);
        if(s[0]=='0'){
            dp[0]=true;
        }else{
            return false;
        }
        while(l<n){
            if(!dp[l]){
                l++;
                continue;
            }
            for(int i=l+minJump;i<=min(l + maxJump,n- 1);i++){
                dp[i] = (s[i] == '0') ? true : dp[i];   
            }
            l+=minJump;
        }
        return dp[n-1];

        
    }
};