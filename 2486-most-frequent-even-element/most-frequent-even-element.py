class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=1000000
        max=0
        l=[]
        for i in nums:
            if(i in l):
                continue
            if(i%2==0):
                if(nums.count(i)>max):
                    max=nums.count(i)
                    min=i
                elif (nums.count(i)==max):
                    if(i<min):
                        min=i
            l.append(i)
        if(min!=1000000):
            return min
        return -1
        