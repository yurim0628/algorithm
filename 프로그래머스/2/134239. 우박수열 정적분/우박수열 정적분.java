import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        List<Integer> sequence = new ArrayList<>();
        sequence.add(k);
        while (k != 1) {
            if (k % 2 == 0) {
                k /= 2;
            } else {
                k = k * 3 + 1;
            }
            sequence.add(k);
        }

        int n = sequence.size();  
        double[] area = new double[n - 1];  

        for (int i = 0; i < n - 1; i++) {
            area[i] = (sequence.get(i) + sequence.get(i + 1)) / 2.0;
        }

        double[] result = new double[ranges.length];
        for (int i = 0; i < ranges.length; i++) {
            int a = ranges[i][0];
            int b = ranges[i][1];
            int start = a;
            int end = (n - 1) + b;  

            if (start > end) {
                result[i] = -1.0;
                continue;
            }

            double sum = 0.0;
            for (int j = start; j < end; j++) {
                sum += area[j];
            }
            result[i] = sum;
        }

        return result;
    }
}
