class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(len(nums)==3):
            return nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3];
        a,b,c=nums[len(nums)-1],nums[len(nums)-2],nums[len(nums)-3]
        if(len(nums)!=4):
            d,e=nums[0],nums[1];
        else:
            r=a*b*c
            h=a*nums[0]*nums[1]
            if(r>h):
                return r
            else:
                return h
        
        r=a*b*c
        h = d*e*a
        if(r>h):
            return r
        else:
            return h

       
        
            