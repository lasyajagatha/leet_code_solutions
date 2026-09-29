class Solution {
    public int smallestIndex(int[] a) {
      int i,s=0;
      for(i=0;i<a.length;i++){
        s=0;
        while(a[i]>0){
            s=s+a[i]%10;
            a[i]=a[i]/10;
        }
        System.out.println(s);
        if(i==s){
            return i;
        }
      }
      return -1;
    }
}