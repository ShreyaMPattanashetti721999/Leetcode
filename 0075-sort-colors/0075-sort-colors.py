class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lo = 0
        hi = n - 1
        mid = 0

    # Iterate till all the elements are sorted
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo = lo + 1
                mid = mid + 1
        
            elif nums[mid] == 1:
                mid = mid + 1
        
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi = hi - 1
        
        return nums
        