class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs=0
        count={}
        for num in nums:
            if num in count:
                pairs+=count[num]
                count[num] +=1      
            else:
                count[num] =1        

        return pairs
