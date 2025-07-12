class Solution {
    public int solution(int[] common) {
        int len = common.length;

        int diff = common[1] - common[0];
        if (common[2] - common[1] == diff) {
            return common[len - 1] + diff;
        } else {
            int ratio = common[1] / common[0];
            return common[len - 1] * ratio;
        }
    }
}
