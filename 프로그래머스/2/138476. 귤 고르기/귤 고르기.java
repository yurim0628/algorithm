import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Long> sizeFrequencyMap = Arrays.stream(tangerine)
            .boxed()
            .collect(Collectors.groupingBy(size -> size, Collectors.counting()));

        List<Map.Entry<Integer, Long>> sortedEntries = sizeFrequencyMap.entrySet().stream()
            .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
            .collect(Collectors.toList());

        int varietyCount = 0;
        for (Map.Entry<Integer, Long> entry : sortedEntries) {
            k -= entry.getValue();
            varietyCount++;
            if (k <= 0) break;
        }

        return varietyCount;
    }
}
