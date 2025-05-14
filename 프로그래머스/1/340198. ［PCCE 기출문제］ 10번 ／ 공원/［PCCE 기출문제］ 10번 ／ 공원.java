import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int n = park.length;
        int m = park[0].length;
        
        Integer[] matsInteger = Arrays.stream(mats)
                              .boxed()
                              .toArray(Integer[]::new);
        Arrays.sort(matsInteger, Collections.reverseOrder());

        for (int mat : matsInteger) {
            for (int i = 0; i <= n - mat; i++) {
                for (int j = 0; j <= m - mat; j++) {
                    if (canPlaceMat(park, i, j, mat)) {
                        return mat;
                    }
                }
            }
        }

        return -1;
    }

    private boolean canPlaceMat(String[][] park, int startX, int startY, int size) {
        for (int i = startX; i < startX + size; i++) {
            for (int j = startY; j < startY + size; j++) {
                if (!park[i][j].equals("-1")) {
                    return false;
                }
            }
        }
        return true;
    }
}
