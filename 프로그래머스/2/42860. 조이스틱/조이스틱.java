class Solution {
    public int solution(String name) {
         int length = name.length();
        int answer = 0;

        for (int i = 0; i < length; i++) {
            char c = name.charAt(i);
            int upDown = Math.min(c - 'A', 'Z' - c + 1);
            answer += upDown;
        }

        int minMove = length - 1; 

        for (int i = 0; i < length; i++) {
            int next = i + 1;

            while (next < length && name.charAt(next) == 'A') {
                next++;
            }

            int move = (i * 2) + (length - next);
            int reverseMove = (length - next) * 2 + i;

            minMove = Math.min(minMove, Math.min(move, reverseMove));
        }

        return answer + minMove;
    }
}