class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u=max(nums)
        v=min(nums)
        for i in nums:
            if(i!=u and i!=v):
                return i
        return -1
        