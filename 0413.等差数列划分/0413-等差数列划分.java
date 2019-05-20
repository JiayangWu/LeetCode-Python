class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int n = A.length;
        
        int sum = 0;
        int[] dp = new int[n];
        for (int i = 2; i < n; i++){
            if (A[i - 1] - A[i - 2] == A[i] - A[i - 1]){
                dp[i] = dp[i - 1] + 1;
                sum += dp[i];
            }
        }
        return sum;
    }
}