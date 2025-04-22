import java.util.*;

class Solution {

    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        List<String> setA = generateSet(str1);
        List<String> setB = generateSet(str2);

        double jaccard = calculateJaccard(setA, setB);

        return (int) (jaccard * 65536);
    }

    private List<String> generateSet(String str) {
        List<String> set = new ArrayList<>();
        for(int i = 0; i < str.length() - 1; i++) {
            char c1 = str.charAt(i);
            char c2 = str.charAt(i + 1);
            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                set.add("" + c1 + c2);
            }
        }
        Collections.sort(set);
        return set;
    }

    private double calculateJaccard(List<String> setA, List<String> setB) {
        List<String> intersection = new ArrayList<>();
        List<String> union = new ArrayList<>();

        for(String s : setA) {
            if (setB.contains(s)) {
                setB.remove(s);
                intersection.add(s);
            }
            union.add(s);
        }
        
        for(String s : setB) {
            union.add(s);
        }

        if (union.size() == 0) {
            return 1.0;
        } else {
            return (double) intersection.size() / union.size();
        }
    }
}