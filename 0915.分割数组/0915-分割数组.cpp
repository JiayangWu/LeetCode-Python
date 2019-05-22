class Solution {
public:
    int partitionDisjoint(vector<int>& a) {
        vector<int> b = a;
        for (int i = a.size() - 2; i >= 0; i--) {
            b[i] = min(b[i], b[i + 1]);
        }
        for (int i = 0, mx = 0; i < a.size(); i++) {
            mx = max(mx, a[i]);
            if (mx <= b[i + 1]) return i + 1;
        }
    }
};