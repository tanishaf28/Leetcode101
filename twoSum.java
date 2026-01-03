class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> t = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            t.put(nums[i],i);
        }
        for (int i=0;i<nums.length;i++){
        int y= target - nums[i];
            if (t.containsKey(y) && t.get(y)!=i) {
                return new int[] {i, t.get(y)};
            }
        }
        throw new IllegalArgumentException("No valid solution");
    }
}
