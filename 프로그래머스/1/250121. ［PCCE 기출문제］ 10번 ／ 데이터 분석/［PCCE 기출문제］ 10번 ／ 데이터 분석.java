import java.util.*;

enum Field {
    CODE(0),
    DATE(1),
    MAXIMUM(2),
    REMAIN(3);

    private final int index;

    Field(int index) {
        this.index = index;
    }

    public int getIndex() {
        return index;
    }

    public static Field fromString(String name) {
        return Field.valueOf(name.toUpperCase());
    }
}

public class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Field extField = Field.fromString(ext);
        Field sortByField = Field.fromString(sort_by);

        int extIndex = extField.getIndex();
        int sortByIndex = sortByField.getIndex();

        List<int[]> filteredList = new ArrayList<>();
        for (int[] d : data) {
            if (d[extIndex] < val_ext) {
                filteredList.add(d);
            }
        }

        filteredList.sort(Comparator.comparingInt(a -> a[sortByIndex]));

        int[][] answer = new int[filteredList.size()][];
        for (int i = 0; i < filteredList.size(); i++) {
            answer[i] = filteredList.get(i);
        }

        return answer;
    }
}