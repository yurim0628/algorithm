import java.util.*;

class Solution {
    int result = 0;
    int[][] inputNumber;
    int[] matchCount;

    public int solution(int n, int[][] q, int[] ans) {
        this.inputNumber = q;
        this.matchCount = ans;

        List<Integer> candidates = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            candidates.add(i);
        }

        combination(candidates, new ArrayList<>(), 0, 5);
        return result;
    }

    private void combination(List<Integer> candidates, List<Integer> currentCombination, int start, int codeLength) {
        if (currentCombination.size() == codeLength) {
            if (check(currentCombination)) {
                result++;
            }
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            currentCombination.add(candidates.get(i));
            combination(candidates, currentCombination, i + 1, codeLength);
            currentCombination.remove(currentCombination.size() - 1);
        }
    }

    private boolean check(List<Integer> code) {
        for (int i = 0; i < inputNumber.length; i++) {
            int count = 0;
            for (int num : inputNumber[i]) {
                if (code.contains(num)) {
                    count++;
                }
            }
            if (count != matchCount[i]) return false;
        }
        return true;
    }
}
