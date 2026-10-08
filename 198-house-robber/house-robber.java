import java.util.Arrays;
class Solution {
    public int rob(int[] nums) {
        int[] a=new int[nums.length];
        int i;
        a[0]=nums[0];
        for(i=1;i<nums.length;i++){
            if(i-2>=0)
                a[i]=Math.max(a[i-1],nums[i]+a[i-2]);
            else
                a[i]=Math.max(a[i-1],nums[i]);
        }
        Arrays.sort(a);
        return a[a.length-1];
    }
}