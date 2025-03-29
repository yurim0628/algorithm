class Solution {
    private boolean isPuzzleSolvable(int[] diffs, int[] times, long level, long limit) {
        long totalTime = calculateTotalTime(diffs, times, level);
        return totalTime <= limit;
    }
    
    private long calculateTotalTime(int[] diffs, int[] times, long level) {
        long totalTime = times[0];

        for (int i = 1; i < times.length; i++) {
            totalTime += times[i];

            if (diffs[i] > level) {
                long iterationCount = diffs[i] - level;
                totalTime += (times[i] + times[i - 1]) * iterationCount;
            }
        }

        return totalTime;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        long low = 1;
        long high = limit;
        
        while (low < high) {
            long mid = (low + high) / 2;
            if (isPuzzleSolvable(diffs, times, mid, limit)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        
        return (int) low;
    }
}
