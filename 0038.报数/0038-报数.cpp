class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        if (n == 2) return "11";
        int i = 2, j = 0;
        string temp = "";
        string res = "11";
        
        for (i; i <n; ++ i ){ // No. i
            j = 0;
            temp = "";
            for (j; j < res.size(); ){
                int k = 0;
                while(j + k < res.size() && res[j] == res[j+k])
                    k += 1;
                temp += to_string(k) + res[j];
                // cout << res[j]<<endl;
                // cout << to_string(res[j] - '0')<<endl;
                // cout <<temp<<endl;
                j+= k;
            }
            res = temp;
            // cout <<res<<endl;
        } 
        return res;
        
    }
};