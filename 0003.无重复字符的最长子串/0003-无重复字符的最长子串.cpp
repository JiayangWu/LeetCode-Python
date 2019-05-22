class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    
        string dic = "";
        int ans = 0;
        int i = 0;
        int j = 0;
        int l = s.size();
        while( i < l && j < l ){
            char a = s[i];
            char b = s[j];
            // cout<<dic.find(b)<<endl;
            if (dic.find(b) >= 0 && dic.find(b) < 99999999){
                i += 1;
                dic.erase(0, 1); 
            }
            else{
                j += 1;
                dic.push_back(b);
                // cout << "Dasdas" << endl;
            }
            ans = ans < j-i ? j-i : ans;
            // cout <<i<<" "<<j << endl;
        }
        return ans;
    }
};