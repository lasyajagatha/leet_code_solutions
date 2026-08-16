class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m=len(nums1)
        n=len(nums2)
        l=[]
        if(m<n):
            for i in nums1:
                if(i in nums2):
                    l.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if(i in nums1):
                    l.append(i)
                    nums1.remove(i)
                    
        return l