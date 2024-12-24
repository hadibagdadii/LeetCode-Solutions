class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif nums[0] < nums[len(nums)-1]:
            return nums[0]

        mid = len(nums) // 2
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] < nums[0]:
            return self.findMin(nums[:mid])
        else:
            return self.findMin(nums[mid:])

        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return min(nums)
        # elif nums[(len(nums)/2)-1] > nums[(len(nums)/2)]:
        #     return nums[(len(nums)/2)]
        # elif nums[(len(nums)/2)] < nums[0]:
        #     return findMin(nums[:(len(nums)/2)])
        # else:
        #     return findMin(nums[(len(nums)/2):])
        
