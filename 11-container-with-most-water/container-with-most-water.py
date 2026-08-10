def minl(u,v):
    if(u<v):
        return u
    return v
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        m=0
        while l<r:
            a=(r-l)*minl(height[r],height[l])
            if(a>m):
                m=a
            if(height[l]>height[r]):
                r=r-1
            else:
                l=l+1
        return m
        
        
         
