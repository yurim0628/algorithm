public class Solution {
    public int solution(String[] babbling) {
        int count = 0;
        String[] words = {"aya", "ye", "woo", "ma"};

        for (String str : babbling) {
            for (String word : words) {
                str = str.replace(word, " ");
            }
            if (str.trim().isEmpty()) {
                count++;
            }
        }
        return count;
    }
}
