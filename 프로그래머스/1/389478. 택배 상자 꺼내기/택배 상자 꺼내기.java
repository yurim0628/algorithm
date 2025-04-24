class Solution {
    public int solution(int n, int w, int num) {
        int totalRow = (int) Math.ceil(n / (double) w);
        int currentRow = (int) Math.ceil(num / (double) w);

        if (totalRow == currentRow) {
            return 1;
        }

        int currentNumber = num;
        int currentPosition = (currentRow * w) - currentNumber;
        int answer = 1;

        for (int i = currentRow; i < totalRow; i++) {
            currentNumber += 2 * currentPosition + 1;
            currentPosition = w - currentPosition - 1; 
            answer++;
        }

        return currentNumber > n ? answer - 1 : answer;
    }
}
