class Solution {
    public int climbStairs(int n, int[] costs) {
        int[] a=new int[n+1];
        a[0]=0;
        if(n==1)
            return costs[0]+1;
        a[1]=costs[0]+1;
        a[2]=Math.min(a[1]+1+costs[1],a[0]+4+costs[1]);
        for(int i=3;i<=n;i++){
            if(a[i-1]+1+costs[i-1]<=a[i-2]+4+costs[i-1] && a[i-1]+1+costs[i-1]<=a[i-3]+9+costs[i-1]){
                a[i]=a[i-1]+1+costs[i-1];
            }else if(a[i-2]+4+costs[i-1] <=a[i-1]+1+costs[i-1] && a[i-2]+4+costs[i-1]<=a[i-3]+9+costs[i-1]){
                a[i]=a[i-2]+4+costs[i-1];
            }else{
                a[i]=a[i-3]+9+costs[i-1];
            }
        }
        return a[n];
    }
}