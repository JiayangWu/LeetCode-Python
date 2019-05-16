class Solution {
    public int[] swap(int ary[]) {
    int len = ary.length;
    for (int i = 0; i < len / 2; i++) {
        int tmp = ary[i];
        ary[i] = ary[len - 1 - i];
        ary[len - 1 - i] = tmp;
    }
    return ary;
}

    public String[] findRelativeRanks(int[] nums) {
        int n = nums.length;
        int[] nums1 = Arrays.copyOf(nums, n);
        String[] result = new String[n];
        
        Arrays.sort(nums1);
        nums1 = swap(nums1);
        Map<Integer, Integer> map = new HashMap<>();
       
        for (int i = 0; i < n; i++){
            map.put(nums[i], i);
    }
        // System.out.println(Arrays.toString(nums1));
        
        for (int i = 0; i < n; i++){
            if (i == 0){
                result[map.get(nums1[i])] = "Gold Medal";
                continue;
            }
            else if (i == 1){
                result[map.get(nums1[i])] = "Silver Medal";
                continue;
            }
            else if (i == 2){
                result[map.get(nums1[i])] = "Bronze Medal";
                continue;
            }
            result[map.get(nums1[i])] = String.valueOf(i + 1);
        }
        return result;
    }
}