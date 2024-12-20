class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {} 
        for idx,n in enumerate(nums) :
            y = target - n
            if y in myDict:
                z = myDict[y]
                return [idx,z]
            myDict[n] = idx
        return [0,0]
