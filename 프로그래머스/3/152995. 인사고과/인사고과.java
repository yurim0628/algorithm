import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int[] wanho = scores[0];

        Arrays.sort(scores, (a, b) -> {
            if (a[0] != b[0]) return b[0] - a[0];
            return a[1] - b[1];
        });

        int maxPeer = 0;
        List<int[]> qualified = new ArrayList<>();

        for (int[] score : scores) {
            if (score[1] < maxPeer) {
                if (Arrays.equals(score, wanho)) return -1; 
                continue; 
            }
            maxPeer = Math.max(maxPeer, score[1]);
            qualified.add(score);
        }

        qualified.sort((a, b) -> (b[0] + b[1]) - (a[0] + a[1]));

        int rank = 1;
        int prevSum = -1;
        int sameCount = 0;

        for (int i = 0; i < qualified.size(); i++) {
            int[] score = qualified.get(i);
            int sum = score[0] + score[1];

            if (sum != prevSum) {
                rank += sameCount;
                sameCount = 1;
                prevSum = sum;
            } else {
                sameCount++;
            }

            if (Arrays.equals(score, wanho)) {
                return rank;
            }
        }

        return -1; 
    }
}
