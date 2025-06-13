class Solution {
    public int[] solution(long begin, long end) {
        final int MAX = 10000000;
        int size = (int)(end - begin + 1);
        int[] answer = new int[size];

        for (long i = begin; i <= end; i++) {
            int idx = (int)(i - begin);

            if (i == 1) {
                answer[idx] = 0;
                continue;
            }

            int maxDivisor = 1;

            for (int d = 2; d <= Math.sqrt(i); d++) {
                if (i % d == 0) {
                    long pair = i / d;

                    if (pair <= MAX) {
                        maxDivisor = (int)pair;
                        break; 
                    }

                    if (d <= MAX) {
                        maxDivisor = Math.max(maxDivisor, d);
                    }
                }
            }

            answer[idx] = maxDivisor;
        }

        return answer;
    }
}
