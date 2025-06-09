class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder allNumbers = new StringBuilder();
        int num = 0;

        while (allNumbers.length() < t * m) {
            allNumbers.append(Integer.toString(num++, n).toUpperCase());
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < t; i++) {
            result.append(allNumbers.charAt(i * m + (p - 1)));
        }

        return result.toString();
    }
}