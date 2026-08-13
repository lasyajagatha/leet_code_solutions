class Solution {
    public int maxProduct(int[] nums) {
        int l=nums[0],m,r=nums[nums.length-1],i,lp=1,rp=1,j;
        if(nums.length==1){
            return nums[0];
        }
        if(l>r)
            m=l;
        else
            m=r;
        for(i=1;i<nums.length;i++){
              if(l==0){
                l=1;
              }
              if(r==0){
                r=1;
              }
              l=l*nums[i];
              j=nums.length-i-1;
              r=r*nums[j];
              if(l>m){
                m=l;
              }
              if(r>m){
                m=r;
              }
        }
       
        return m;
    }
}