class Solution:
    def sets(self,nums: List[int],ind : int,ans :List[List[int]],temp:list[int]):
        if ind==len(nums):
            ans.append(temp.copy())
            return
        temp.append(nums[ind])
        self.sets(nums,ind+1,ans,temp)
        temp.pop()
        self.sets(nums,ind+1,ans,temp)
        return 

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.sets(nums,0,ans,[])

        return ans

        