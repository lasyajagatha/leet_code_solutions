class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        nums2=[]
        for i in range(0,len(nums1)):
            if(i+1<len(nums1) and nums1[i]%2==0 and nums1[i+1]%2!=0):
                nums2.append(nums1[i]-nums1[i])
            else:
                nums2.append(nums1[i])
        return True
        