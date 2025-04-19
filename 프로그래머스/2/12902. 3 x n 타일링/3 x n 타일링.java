public class Solution {
    public int solution(int n) {
        if (n % 2 != 0) return 0; 

        int MOD = 1000000007;
        int index = n / 2;

        int[] answer = new int[index + 1];
        answer[0] = 0;
        if (index >= 1) answer[1] = 3;
        if (index >= 2) answer[2] = 11;

        if (index < 3) return answer[index];

        for (int i = 3; i <= index; i++) {
            long sum = 0;
            for (int j = 1; j <= i - 2; j++) {
                sum = (sum + answer[j]) % MOD;
            }
            answer[i] = (int)((3L * answer[i - 1] + 2L * sum + 2) % MOD);
        }

        return answer[index];
    }
}
