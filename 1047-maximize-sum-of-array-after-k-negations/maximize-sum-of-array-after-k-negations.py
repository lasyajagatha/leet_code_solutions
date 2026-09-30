class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        while(k!=0):
            nums[0]=-nums[0]
            nums.sort()
            k=k-1
        return sum(nums)


        