class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size();
        int n=matrix[0].size();

        int i=0;

        while (i<m){
            if (matrix[i][0]<=target && target<=matrix[i][n-1]){
                int l=0,r=n-1;
                int mid=l+(r-l)/2;
                while(l<=r){
                    if(matrix[i][mid]==target){
                        return true;
                    }
                    else if(matrix[i][mid]<target){
                        l=mid+1;
                    }
                    else{
                        r=mid-1;
                    }
                    mid = l + (r - l) / 2;
                }
            }
            i+=1;

        } 
        return false;     
    }
};
