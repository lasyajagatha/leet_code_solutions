class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l=0,r=numbers.length-1;
        int[] c=new int[2];
        while(l<r){
            if(numbers[l]+numbers[r]==target){
                     c[0]=l+1;
                     c[1]=r+1;
                     return c;
            } else if(numbers[l]+numbers[r] > target){
                r=r-1;
            } else{
                l=l+1;
            }
        }
        return c;
    }
}