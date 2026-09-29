class Solution {
    public int smallestNumber(int n, int t) {
        int i,s=0,p;
        for(i=n;i<=n+100;i++){
            s=i;
            p=1;
            while(s>0){
            p*=s%10;
            s=s/10;
            }
            if(p%t==0){
                return i;
            }

        }
        return -1;
    }
}