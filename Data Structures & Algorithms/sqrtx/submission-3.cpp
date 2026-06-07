class Solution {
public:
    int mySqrt(int x) {
        int l=0,r=x;
        int mid;
        while(l<=r){
            mid=(l+r)/2;
            long long temp = (long long)mid * mid;;
            if(temp==x){
                return mid;
            }
            else if(temp>x){
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return (l+r)/2;
        
    }
};