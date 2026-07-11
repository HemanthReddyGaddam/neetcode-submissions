class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) return 1;

        int l = 0, r = 1;
        int ans = 1;
        char prev = ' ';  

        while (r < n) {
            if (arr[r - 1] > arr[r] && prev != '>') {
                ans = max(ans, r - l + 1);
                prev = '>';
                r++;
            }
            else if (arr[r - 1] < arr[r] && prev != '<') {
                ans = max(ans, r - l + 1);
                prev = '<';
                r++;
            }
            else {
                if (arr[r] == arr[r - 1])
                    r++;
                l = r - 1;
                prev = ' ';
            }
        }

        return ans;
    }
};