public class Solution {
    public int solution(int[][] sizes) {
        int w = 1;
        int h = 1;

        for (int[] size : sizes) {
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);

            w = Math.max(w, width);
            h = Math.max(h, height);
        }

        return w * h;
    }
}
