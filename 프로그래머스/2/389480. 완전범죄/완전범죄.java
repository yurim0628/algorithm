class Solution {
    public int solution(int[][] info, int n, int m) {
        int len = info.length;
        int INF = 120;
        int[][] memo = new int[len][m];
        
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < m; j++) {
                memo[i][j] = INF;
            }
        }

        if (info[0][0] < n)
            memo[0][0] = info[0][0];
        if (info[0][1] < m)
            memo[0][info[0][1]] = 0;

        for (int i = 1; i < len; i++) {
            for (int j = 0; j < m; j++) {
                if (memo[i - 1][j] >= INF) continue;

                int newA = memo[i - 1][j] + info[i][0];
                if (newA < n) {
                    memo[i][j] = Math.min(memo[i][j], newA);
                }

                int newB = j + info[i][1];
                if (newB < m) {
                    memo[i][newB] = Math.min(memo[i][newB], memo[i - 1][j]);
                }
            }
        }

        int minA = INF;
        for (int j = 0; j < m; j++) {
            minA = Math.min(minA, memo[len - 1][j]);
        }

        return minA >= n ? -1 : minA;
    }
}
