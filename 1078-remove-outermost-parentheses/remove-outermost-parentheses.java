import java.util.LinkedList;
class Solution {
    public String removeOuterParentheses(String s) {
        LinkedList<Integer> n=new LinkedList<>();
        LinkedList<Integer> k=new LinkedList<>();
        int i=0;
        for(i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                n.addFirst(i);
            } else {
                int m=n.removeFirst();
                if(n.isEmpty()){
                    k.add(m);
                    k.add(i);
                    System.out.println(m + " "+ i);
                }
            }
        }
        String res="",rap;
        StringBuffer r=new StringBuffer(res);
        for(i=0;i<s.length();i++){
            if(i==k.getFirst()){
                k.removeFirst();
            }else{
                r.append(s.charAt(i));
            }
        }
        rap=r.toString();
        return rap;
        
    }
}