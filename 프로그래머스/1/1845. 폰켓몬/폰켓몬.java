import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int numLength = nums.length/2;
        int numLength2 = 0;
            
        Set<Integer> nums2 = new HashSet<>();
        
        for(int num : nums) {
            nums2.add(num);
        }
        numLength2 = nums2.size();
        
        if(numLength2 >= numLength) {
            answer = numLength;
        } else {
            answer = numLength2;
        }
        
       
        
        
        return answer;
    }
}