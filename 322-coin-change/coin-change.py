class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]*(amount+1)
        dp[0]=0
        coins.sort()
        for i in range(1,amount+1):
            l=[]
            l.append(dp[i])
            j,x=0,0
            while(j<len(coins) and i>=coins[j]):
                x=1+dp[i-coins[j]]
                l.append(x)
                j=j+1
            dp[i]=min(l)
        if(dp[amount]!=amount+1 or amount==0):
            return dp[amount]
        return -1

