class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0,i,r=0,c=0,m=0;
        while(r<nums.length){
            if(nums[r]==0){
                c=c+1;
            }
            while(c>k){
                if(nums[l]==0)
                    c=c-1;
                l=l+1;
                }
            if(m<r-l+1){
                m=r-l+1;
            }
            r++;
        }
        return m;
    }
}