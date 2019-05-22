class Solution {
public:
    int firstUniqChar(string s) {
        string dic = "abcdefghijklmnopqrstuvwxyz";
        int res = s.size();
        for (int i = 0; i < dic.size(); ++i){
            int a = s.find(dic[i]);
            int b = s.rfind(dic[i]);
            cout << a <<" " << b <<endl;
            if (a == b && a != -1){
                res = a<res ? a :res;
            }
        }
        return res < s.size() ? res : -1;
    }
};