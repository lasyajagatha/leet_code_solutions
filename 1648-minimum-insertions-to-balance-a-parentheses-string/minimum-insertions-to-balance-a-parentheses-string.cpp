#include<stack>
class Solution {
public:
    int minInsertions(string s) {
        stack<char> k;
        int i=0,j,c=0,h=0;
        while(i<s.length()){
            if(s[i]=='('){
                k.push('(');
                i=i+1;
            } else{
                if(i+1>=s.length() ){
                    if(k.size()!=0){
                        k.pop();
                        c=c+1;
                    }else{
                        c=c+2;
                    }
                    i=i+1;
                }else if( k.size()==0 ){
                    c=c+1;
                    if(s[i+1]==')'){
                        i=i+2;
                    } else{
                        c=c+1;
                        i=i+1;
                    }
                } else{
                    k.pop();
                    if(s[i+1]==')')
                        i=i+2;
                    else{
                        c=c+1;
                    i=i+1;
                    }
                }
                }
        }
        while(k.size()>0){
            c=c+2;
            k.pop();
        }
        return c;
    }
};