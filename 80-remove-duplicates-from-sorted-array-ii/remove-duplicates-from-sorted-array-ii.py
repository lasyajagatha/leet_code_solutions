class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=len(nums)
        l=[]
        for i in nums:
            if(i not in l):
                if(nums.count(i)>=2):
                    l.append(i)
                    l.append(i)
                else:
                    l.append(i)
        for i in range(0,len(l)):
            nums[i]=l[i]
        return len(l)
            


            
            
        