class Solution {
    public int[] solution(int[][] arr) {
        return compress(arr, 0, 0, arr.length);
    }
    
    private int[] compress(int[][] arr, int sx, int sy, int length) {
        int[] elementCount = countElements(arr, sx, sy, length);

        if (elementCount[0] == 0) return new int[]{0, 1}; 
        if (elementCount[1] == 0) return new int[]{1, 0}; 

        int halfLength = length / 2;

        int[] topLeft = compress(arr, sx, sy, halfLength);
        int[] topRight = compress(arr, sx, sy + halfLength, halfLength);
        int[] bottomLeft = compress(arr, sx + halfLength, sy, halfLength);
        int[] bottomRight = compress(arr, sx + halfLength, sy + halfLength, halfLength);

        return new int[]{
            topLeft[0] + topRight[0] + bottomLeft[0] + bottomRight[0], 
            topLeft[1] + topRight[1] + bottomLeft[1] + bottomRight[1]
        };
    } 

    private int[] countElements(int[][] arr, int sx, int sy, int length) {
        int countZero = 0;
        int countOne = 0;

        for (int i = sx; i < sx + length; i++) {
            for (int j = sy; j < sy + length; j++) {
                if (arr[i][j] == 0) countZero++;
                else countOne++;
            }
        }

        return new int[]{countZero, countOne};
    }
}
