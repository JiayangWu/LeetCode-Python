class Solution {
    public String[] findRelativeRanks(int[] nums) {
        int n = nums.length;
        int[] nums1 = Arrays.copyOf(nums, n);
        String[] result = new String[n];
        
        Arrays.sort(nums1);
        Map<Integer, Integer> map = new HashMap<>();
       
        for (int i = 0; i < n; i++){
            map.put(nums[i], i);
    }
        // System.out.println(Arrays.toString(nums1));
        
        for (int i = n - 1; i >=0 ; i--){
            if (i == n - 1)
                result[map.get(nums1[i])] = "Gold Medal";
            else if (i == n - 2)
                result[map.get(nums1[i])] = "Silver Medal";
            else if (i == n - 3)
                result[map.get(nums1[i])] = "Bronze Medal";
            else
                result[map.get(nums1[i])] = String.valueOf(n - i);
        }
        return result;
    }
}