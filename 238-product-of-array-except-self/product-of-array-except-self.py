class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        r=[]
        p=1
        a=1
        if(0 not in nums):
            for i in nums:
                p=p*i
            for i in range(0,len(nums)):
                nums[i]=p//nums[i]
        else:
            for i in nums:
                if(i!=0):
                    p=p*i
            if(nums.count(0)>1):
                for i in range(0,len(nums)):
                    nums[i]=0
                return nums
            
            for i in range(0,len(nums)):
                if(nums[i] == 0):
                    nums[i]=p
                else:
                    nums[i]='*'
            for i in range(0,len(nums)):
                if(nums[i]=='*'):
                    nums[i]=0

        return nums
                


        