class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0){
            return 0;
        }
        int lh = haystack.size();
        int ln = needle.size();
        bool flag = 0;
        for (int i = 0; i <=lh - ln ; ++i){
            flag = 1;
            for (int j = i; j < i + ln; ++ j){
                if (haystack[j] != needle[j-i]){
                    flag = 0;
                    break;
                }
            }
            if (flag) return i;
        }
        if (!flag) return -1;
    }
    
};