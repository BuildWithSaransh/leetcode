class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write_index=0
        for num in nums:
         if num!=0:
            nums[write_index]=num
            write_index +=1
        for i in range(write_index,len(nums)):
            nums[i]=0


    
