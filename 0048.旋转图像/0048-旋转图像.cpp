class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int l = matrix[0].size();
        for (int i = 0 ; i < matrix.size(); ++i){
            for (int j = i + 1; j < l; ++j)
                swap(matrix[i][j], matrix[j][i]);
            reverse(matrix[i].begin(), matrix[i].end());
        }
        
    }
};