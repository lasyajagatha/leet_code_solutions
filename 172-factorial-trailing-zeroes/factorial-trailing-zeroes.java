class Solution {
    public int trailingZeroes(int n) {
      int i=0,c=0;
      int p;
      for(i=1;i<(n/2);i++){
           if((n/Math.pow(5,i))<0){
            break;
           }
           p=(int)(n/Math.pow(5,i));
          c=c+p;
      }
      return c;
    }
}