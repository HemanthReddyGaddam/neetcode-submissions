class Solution {
public:
    bool isPalindrome(string s) {
    int left = 0;
    int right = s.size() - 1;

    while (left < right) {
        if (s[left] != s[right])
            return false;
        left++;
        right--;
    }

    return true;
    }
    void result(string s,vector<vector<string>> &ans,vector<string> part,int l,int n){
        if(l>=n){
            ans.push_back(part);
            return;
        }
        for(int i=l;i<n;i++){
            string temp=s.substr(l,i-l+1);
            if(isPalindrome(temp)){
                part.push_back(temp);
                result(s,ans,part,i+1,n);
                part.pop_back();
            }
        }

    }
    vector<vector<string>> partition(string s) {
        int n=s.size();
        vector<string> part;
        vector<vector<string>> ans;
        result(s,ans,part,0,n);
        return ans;
    }
};
