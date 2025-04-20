import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int size = (int)(right - left + 1);
        int[] arr = new int[size];

        for (int i = 0; i < size; i++) {
            long currentIndex = left + i;
            int currentRow = (int)(currentIndex / n);
            int currentCol = (int)(currentIndex % n);
            if(currentRow > currentCol) arr[i] = currentRow + 1;
            else arr[i] = currentCol + 1;
    }

        return arr;
    }
}
