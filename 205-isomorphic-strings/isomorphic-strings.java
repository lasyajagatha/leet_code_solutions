class Solution {
    public boolean isIsomorphic(String s, String t) {
       int i,j;
       char u,v;
       for(i=0;i<s.length();i++){
        u=s.charAt(i);
        v=t.charAt(i);
         for(j=i+1;j<s.length();j++){
              if(s.charAt(j)==u && t.charAt(j)!=v){
                return false;
              }
              if(s.charAt(j)!=u && t.charAt(j)==v){
                return false;
              }

         }
       } 
       return true;
    }
}