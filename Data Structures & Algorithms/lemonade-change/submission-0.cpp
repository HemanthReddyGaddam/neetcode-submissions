class Solution {
public:
    bool lemonadeChange(vector<int>& bill) {
        vector<int> dp(3,0);
        unordered_map<int,int> mp;
        mp.insert({5,0});
        mp.insert({10,0});
        mp.insert({20,0});
        for(int i=0;i<bill.size();i++){
            mp[bill[i]]++;
            if(bill[i]==10){
                if(mp[5]==0){
                    return false;
                }
                mp[5]--;
            }
            else if(bill[i]==20){
                if(mp[5]==0){
                    return false;
                }
                if(mp[10]){
                    mp[10]--;
                    mp[5]--;
                    continue;
                }
                else if(mp[5]-3<0){
                    return false;
                }
                mp[5]-=3;
            }
            
        }
        return true;
    }
};