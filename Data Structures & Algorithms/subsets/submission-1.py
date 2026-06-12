class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, temp):
            ans.append(temp.copy())

            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])
        return ans