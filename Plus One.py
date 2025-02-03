class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        multiple = 1
        total = 0
        result = []

        for num in reversed(digits):
            total = total + (num * multiple)
            multiple = multiple * 10
        
        total += 1

        for num in str(total):
            result.append(int(num))

        return result
