import java.util.*;

class Solution {
    public int solution(int[] toppings) {
        int answer = 0;

        Map<Integer, Integer> rightMap = new HashMap<>();
        for (int topping : toppings) {
            rightMap.put(topping, rightMap.getOrDefault(topping, 0) + 1);
        }

        Map<Integer, Integer> leftMap = new HashMap<>();
        int leftTypes = 0;
        int rightTypes = rightMap.size();

        for (int topping : toppings) {
            leftMap.put(topping, leftMap.getOrDefault(topping, 0) + 1);
            if (leftMap.get(topping) == 1) {
                leftTypes++;
            }

            rightMap.put(topping, rightMap.get(topping) - 1);
            if (rightMap.get(topping) == 0) {
                rightMap.remove(topping);
                rightTypes--;
            }

            if (leftTypes == rightTypes) {
                answer++;
            }
        }

        return answer;
    }
}
