class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[0 for i in range(len(nums))]
        for i in range(0,len(nums)):
            for j in range(1+i,nums[i]+1+i):
                if(j>len(nums)-1):
                    break
                if(a[j]==0):
                    a[j]=1+a[i]
                else:
                    a[j]=a[j] if a[j]<a[i]+1 else a[i]+1
        return a[len(nums)-1]