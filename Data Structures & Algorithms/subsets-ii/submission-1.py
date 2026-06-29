class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        def subs(temp,ind):
            if ind==len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[ind])
            subs(temp,ind+1)
            temp.pop()

            while ind<len(nums)-1 and nums[ind]==nums[ind+1]:
                ind+=1
            subs(temp,ind+1)
        subs([],0)
        return ans
            