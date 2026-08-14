class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m=set(nums1)
        n=set(nums2)
        k=m&n
        if(len(k)==0):
            return -1
        return min(k)