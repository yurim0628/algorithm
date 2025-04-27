class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int totalTiles = brown + yellow;
        for (int height = 3; height <= totalTiles; height++) {
            int width = totalTiles / height;

            if (width < 3) {
                continue;
            }

            if (width >= height) {
                int innerArea = (width - 2) * (height - 2);
                if (innerArea == yellow) {
                    answer[0] = width;
                    answer[1] = height;
                    break;
                }
            }
        }
        return answer;
    }
}