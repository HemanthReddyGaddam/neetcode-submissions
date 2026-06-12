class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr_sum, ind, temp):
            if curr_sum > target:
                return

            if curr_sum == target:
                ans.append(temp.copy())
                return
            for i in range(ind,len(nums)):
                temp.append(nums[i])
                dfs(curr_sum + nums[i], i, temp)
                temp.pop()

        dfs(0, 0, [])
        return ans