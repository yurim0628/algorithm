class Solution {
    private int[] answer = new int[2];
    
    public int[] solution(int[][] arr) {
        divideAndCount(arr, 0, 0, arr.length);
        return answer;
    }
    
    private void divideAndCount(int[][] arr, int sx, int sy, int length) {
        boolean isUniform = isUniformBlock(arr, sx, sy, length, arr[sx][sy]);

        if (isUniform) {
            if (arr[sx][sy] == 0) {
                answer[0]++;
            } else {
                answer[1]++;
            }
        } else {
            int halfLength = length / 2;
            divideAndCount(arr, sx, sy, halfLength);
            divideAndCount(arr, sx, sy + halfLength, halfLength);
            divideAndCount(arr, sx + halfLength, sy, halfLength);
            divideAndCount(arr, sx + halfLength, sy + halfLength, halfLength);
        }
    }

    private boolean isUniformBlock(int[][] arr, int sx, int sy, int length, int element) {
        for (int i = sx; i < sx + length; i++) {
            for (int j = sy; j < sy + length; j++) {
                if (arr[i][j] != element) {
                    return false;
                }
            }
        }
        return true;
    }
}