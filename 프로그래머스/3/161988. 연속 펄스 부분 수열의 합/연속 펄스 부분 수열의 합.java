class Solution {
    public long solution(int[] sequence) {
        int n = sequence.length;
        long maxSum = Long.MIN_VALUE;

        long sum1 = 0; 
        long sum2 = 0; 

        for (int i = 0; i < n; i++) {
            int pulse1 = (i % 2 == 0) ? 1 : -1;
            int pulse2 = -pulse1;

            long val1 = sequence[i] * pulse1;
            long val2 = sequence[i] * pulse2;

            sum1 = Math.max(val1, sum1 + val1);
            sum2 = Math.max(val2, sum2 + val2);

            maxSum = Math.max(maxSum, Math.max(sum1, sum2));
        }

        return maxSum;
    }
}
