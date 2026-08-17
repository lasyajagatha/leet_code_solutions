class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=0
        print(c)
        l=[]
        for i in range(0,len(nums)-1):
           
            if(nums[i]==nums[i+1]):
                nums[i]=2*nums[i]
                nums[i+1]=0
                c=c+1
               
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                l.append(nums[i])
        for i in range(len(l),len(nums)):
            l.append(0)
        return l