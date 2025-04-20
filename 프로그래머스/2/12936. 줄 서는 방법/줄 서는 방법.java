import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> numbers = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        k--; 

        for (int i = 0; i < n; i++) {
            long numOfCases = factorial(n - 1 - i);
            int index = (int)(k / numOfCases);
            answer[i] = numbers.get(index);
            numbers.remove(index);
            k %= numOfCases;
        }

        return answer;
    }

    public long factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
}
