class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp={}
        ans=-1
        count=0
        for i,j in trust:
            if j not in mp:
                mp[j]=0
            mp[j]+=1
            if mp[j]==n-1:
                count+=1
                ans=j
        if count!=1:
            return -1
        for i,j in trust:
            if i==ans:
                return -1
        return ans


        