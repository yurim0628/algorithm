class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = schedules.length;

        int sunday = 7 - startday;
        int saturday = (sunday + 6) % 7;

        for (int i = 0; i < schedules.length; i++) {
            int schedule = schedules[i];
            int[] log = timelogs[i];

            int limit = addTenMinutes(schedule);

            for (int j = 0; j < 7; j++) {
                if (j == saturday || j == sunday) continue;
                if (log[j] > limit) {
                    answer--;
                    break;
                }
            }
        }
        return answer;
    }

    private int addTenMinutes(int time) {
        int hour = time / 100;
        int minute = time % 100 + 10;
        if (minute >= 60) {
            hour++;
            minute -= 60;
        }
        return hour * 100 + minute;
    }
}
