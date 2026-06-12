from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0

        total = sum(nums)
        if total < target:
            return 0

        curr_sum = 0
        ans = float('inf')

        while r < n:
            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1

        return ans
            
        