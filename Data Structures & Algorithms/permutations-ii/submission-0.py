class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        used=[0]*n
        ans=[]
        def sets(temp,used):
            if len(temp)==n:
                ans.append(temp.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                temp.append(nums[i])
                used[i]=1
                sets(temp,used)
                used[i]=0
                temp.pop()
        sets([],used)

        return [list(x) for x in set(tuple(x) for x in ans)]
        
        