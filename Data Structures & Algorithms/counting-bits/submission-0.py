class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        for res in range(1,n+1):
            dp[res]=dp[res>>1]+(res&1)
        
        return dp

        