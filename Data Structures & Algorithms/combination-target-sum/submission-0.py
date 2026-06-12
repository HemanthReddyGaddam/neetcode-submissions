class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr_sum, ind, temp):
            if curr_sum > target or ind == len(nums):
                return

            if curr_sum == target:
                ans.append(temp.copy())
                return

            temp.append(nums[ind])
            dfs(curr_sum + nums[ind], ind, temp)
            temp.pop()

            dfs(curr_sum, ind + 1, temp)

        dfs(0, 0, [])
        return ans