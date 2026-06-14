class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        l=1
        while l<k:
            heapq.heappop_max(nums)
            l+=1
        return nums[0]

        