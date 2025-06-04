import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int count = nums.length / 2;
        Set<Integer> numSet = new HashSet<>();
        for(int num : nums) {
            numSet.add(num);
        }
        if (numSet.size() >= count) {
            return count;
        } else {
            return numSet.size();
        }
    }
}