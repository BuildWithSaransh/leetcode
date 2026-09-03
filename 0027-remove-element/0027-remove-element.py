class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        for num in nums:
            if num != val:
                nums[x] = num
                x += 1
        return x
