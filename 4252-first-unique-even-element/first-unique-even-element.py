class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        p=[]
        for i in range(0,len(nums)):
            if(nums[i] not in l and nums[i] not in p):
                l.append(nums[i])
                continue
            if(nums[i] in l):
                 l.remove(nums[i])
            p.append(nums[i])
           
            
        for i in l:
            if(i%2==0):
                return i
        return -1
        