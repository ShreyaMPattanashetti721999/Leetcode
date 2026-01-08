class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxending = nums[0]
        currentmax = nums[0]

        for i in range(1,len(nums)):
            maxending = max(nums[i],maxending + nums[i])
            currentmax = max(currentmax,maxending)

        return currentmax
        