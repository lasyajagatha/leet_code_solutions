class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in arr:
            if(i%2==0):
                r=i//2
                if(r==0):
                    print(arr.count(0))
                    if(arr.count(0)>=2):
                        return True
                if(r in arr and r!=i):
                    return True
        return False
        