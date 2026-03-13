class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest=min(nums)
        greatest=max(nums)
        count=0
        for num in nums:
            if num > smallest and num < greatest :
                count+=1
        
        return count
