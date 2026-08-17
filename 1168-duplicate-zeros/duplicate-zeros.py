class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l=[]
        for i in arr:
            if(i == 0):
                l.append(0)
                l.append(0)
            else:
                l.append(i)
        for i in range(0,len(arr)):
            arr[i]=l[i]
        