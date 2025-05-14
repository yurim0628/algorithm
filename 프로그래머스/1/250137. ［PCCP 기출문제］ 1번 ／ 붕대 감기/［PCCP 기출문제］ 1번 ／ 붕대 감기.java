public class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int maxHealth = health;
        int time = 0;
        int attackIndex = 0;
        int continuousSuccess = 0;

        int lastAttackTime = attacks[attacks.length - 1][0];

        for (time = 1; time <= lastAttackTime; time++) {
            if (attackIndex < attacks.length && time == attacks[attackIndex][0]) {
                health -= attacks[attackIndex][1];
                if (health <= 0) {
                    return -1;
                }
                continuousSuccess = 0;
                attackIndex++;
            } else {
                health += bandage[1];
                continuousSuccess++;
                if (continuousSuccess == bandage[0]) {
                    health += bandage[2];
                    continuousSuccess = 0;
                }
                if (health > maxHealth) {
                    health = maxHealth;
                }
            }
        }

        return health;
    }
}
