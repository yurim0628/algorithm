class Solution {
    public int solution(int n, long l, long r) {
        return (int) countOnes(n, l - 1, r - 1);
    }

    private long countOnes(int n, long l, long r) {
        if (n == 0) {
            return 1;
        }

        long length = (long) Math.pow(5, n);
        long partLength = length / 5;
        long count = 0;

        for (int i = 0; i < 5; i++) {
            long start = i * partLength;
            long end = (i + 1) * partLength - 1;

            if (r < start || l > end) {
                continue;
            }

            if (i == 2) {
                continue;
            }

            long newL = Math.max(0, l - start);
            long newR = Math.min(partLength - 1, r - start);
            count += countOnes(n - 1, newL, newR);
        }

        return count;
    }
}
