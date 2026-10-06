#include<stack>
class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<int> k;
        int i,c=0;
        for(i=0;s[i]!='\0';i++){
            if(s[i]=='('){
                k.push('(');
            } else{
                if(k.empty()){
                    c=c+1;
                } else{
                    k.pop();
                }
            }
        }
        while(!k.empty()){
            c=c+1;
            k.pop();
        }
        return c;
    }
};