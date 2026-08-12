class Solution {
    public int maxSubArray(int[] nums) {
        int m=nums[0],c=nums[0],i;
        for(i=1;i<nums.length;i++){
            if(nums[i] > c+nums[i]){
                c=nums[i];
            } else{
                c=c+nums[i];
            }
            if(c>m){
                m=c;
            }
           
        }
         return m;
    }
}