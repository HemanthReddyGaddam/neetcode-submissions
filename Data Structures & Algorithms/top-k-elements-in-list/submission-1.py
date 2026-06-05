class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        ans=[]
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
        
        arr = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(arr[i][0])

        return ans

        