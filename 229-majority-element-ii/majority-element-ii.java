import java.util.ArrayList;
import java.util.HashMap;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> l=new ArrayList<>();
        HashMap<Integer,Integer> k=new HashMap<>();
        for(int j=0;j<nums.length;j++){
            int i=nums[j];
            if(k.containsKey(i)){
                k.put(i,k.get(i)+1);
            } else{
                k.put(i,1);
            }
            if(k.get(i)>Math.ceil(nums.length/3) && l.contains(i)==false){
                 l.add(i);
            }
        }
        return l;
    }
}