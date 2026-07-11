class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) return 1;

        int inc = 1, dec = 1,ans=1;
        for(int i=0;i<n-1;i++){
            if(arr[i]<arr[i+1]){
                inc=dec+1;
                dec=1;
            }else if(arr[i]>arr[i+1]){
                dec=inc+1;
                inc=1;
            }else{
                dec=1,inc=1;
            }
            ans=max(ans,max(inc,dec));
        }
        return ans;
        
    }
};