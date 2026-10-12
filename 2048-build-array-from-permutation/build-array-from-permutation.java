class Solution {
    public int[] buildArray(int[] nums) {
        int i;
        int[] h=new int[nums.length];
        for(i=0;i<nums.length;i++){
            h[i]=nums[nums[i]];

        }
        return h;
        
    }
}