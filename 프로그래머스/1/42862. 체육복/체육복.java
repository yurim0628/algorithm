import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> reserveSet = new HashSet<>();
        Set<Integer> lostSet = new HashSet<>();

        for (int r : reserve) {
            reserveSet.add(r);
        }
        for (int l : lost) {
            if (reserveSet.contains(l)) {
                reserveSet.remove(l);
            } else {
                lostSet.add(l);
            }
        }

        int answer = n - lostSet.size();
        
        for(int l : lostSet) {
            if(reserveSet.contains(l-1)) {
                answer ++;
                reserveSet.remove(l-1);
            } else if (reserveSet.contains(l+1)) {
                answer ++;
                reserveSet.remove(l+1);
            }
        }
        return answer;
}
}
