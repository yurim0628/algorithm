import java.util.*;

class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        List<Integer> crewTimes = new ArrayList<>();
        for (String time : timetable) {
            String[] split = time.split(":");
            int totalMin = Integer.parseInt(split[0]) * 60 + Integer.parseInt(split[1]);
            crewTimes.add(totalMin);
        }
        Collections.sort(crewTimes);

        int busTime = 540; 
        int crewIndex = 0;
        int lastBusTime = 0;
        int lastCrewTime = 0;

        for (int i = 0; i < n; i++) {
            int count = 0;
            while (crewIndex < crewTimes.size() && crewTimes.get(crewIndex) <= busTime && count < m) {
                lastCrewTime = crewTimes.get(crewIndex);
                crewIndex++;
                count++;
            }

            if (i == n - 1) { 
                if (count < m) {
                    lastBusTime = busTime;
                } else {
                    lastBusTime = lastCrewTime - 1;
                }
            }

            busTime += t;
        }

        return String.format("%02d:%02d", lastBusTime / 60, lastBusTime % 60);
    }
}
