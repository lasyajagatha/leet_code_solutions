class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1,max(arr)*(max(arr)+2)):
            if(i not in arr):
                k=k-1
            if(k==0):
                return i
        return 0

        