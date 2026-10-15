class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        a.append(nums[0])
        b.append(nums[1])
        for i in range(2,len(nums)):
            if(a[len(a)-1]>b[len(b)-1]):
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b        