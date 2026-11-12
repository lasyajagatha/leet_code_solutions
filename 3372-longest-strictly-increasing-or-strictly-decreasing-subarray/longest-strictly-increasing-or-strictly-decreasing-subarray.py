class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c,m=0,1
        for i in range(len(nums)):
            for j in range(i,len(nums)-1):
                if(nums[j]<nums[j+1]):
                   if(j+1-i+1>m):
                    m=j-i+2
                else:
                    break
        for i in range(len(nums)):
            for j in range(i,len(nums)-1):
                if(nums[j]>nums[j+1]):
                   if(j+1-i+1>m):
                     m=j-i+2
                else:
                    break
        return m
        