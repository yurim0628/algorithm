class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            int divisorCount = getDivisorCount(i);
            if (divisorCount > limit) {
                answer += power;
            } else {
                answer += divisorCount;
            }
        }
        return answer;
    }

    private int getDivisorCount(int number) {
        int count = 0;
        for (int i = 1; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                count++; 
                if (i != number / i) {
                    count++; 
                }
            }
        }
        return count;
    }
}