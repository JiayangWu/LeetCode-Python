#include <cctype>
class Solution {
public:
    string reverseOnlyLetters(string S) {
        //scount = 0;
        int rpos = S.size();
        int lpos = 0;
        for (int i = 0; i < S.size(); i++){
            if (isalpha(S[i])){
                lpos = i;
                char temp = S[i];
                for (int j = rpos-1; rpos > lpos; j--){
                    if (isalpha(S[j])){
                        //cout<<S[i]<<" "<<S[j]<<endl;
                        S[i] = S[j];
                        S[j] = temp;
                        rpos = j;
                        break;
                    }
                }
                
            }
        }
        return S;
        
    }
};