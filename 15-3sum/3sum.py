class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r,l=0,0
        k=[]
        p=[]
        nums.sort()
        for i in range(0,len(nums)-2):
              l=i+1
              r=len(nums)-1
              t=0-nums[i]
              while(l<r):
                if(nums[l]+nums[r]==t):
                      k.append(nums[i])
                      k.append(nums[l])
                      k.append(nums[r])
                      if(k not in p):
                        p.append(k)
                      k=[]
                      r=r-1
                elif(nums[l]+nums[r] >t):
                    r=r-1
                else:
                    l=l+1
     
        return p