class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        x = n // 2

        freq = {}

        for num in nums:
            freq[num] =  freq.get(num,0) + 1

        sortedKeys = sorted(freq.keys())

        for key in sortedKeys:
            if freq[key] > x:
                return key
                

        